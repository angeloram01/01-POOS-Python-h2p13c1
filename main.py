import sqlite3
from empleado import Empleado
from basedatos import BaseDatos
from clima import mostrar_clima
from login import verificar_login
from monedas import consultar_monedas, convertir_sueldo
from validar_rut import validar_rut, normalizar_rut

db = BaseDatos()

def leer_numero(mensaje: str) -> int:
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

def leer_flotante(mensaje: str) -> float:
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Error: Debe ingresar un número válido.")

def menu():
    print("=" * 30)
    print(" EcoTech Solutions - Gestión")
    print("=" * 30)
    print("1.- Registrar empleado")
    print("2.- Buscar empleado por RUT")
    print("3.- Actualizar empleado")
    print("4.- Eliminar empleado")
    print("5.- Mostrar todos los empleados")
    print("6.- Mostrar el clima")
    print("7.- Consultar tipo de cambio")
    print("8.- Convertir sueldo a otra moneda")
    print("9.- Convertir sueldo de empleado por RUT")
    print("0.- Salir")
    
    op = leer_numero("Ingrese una opción: ")

    if op < 0 or op > 9:
        print("Error: Debe ingresar una opción entre 0 y 9.")
        return -1

    return op


def leer_rut(mensaje):
    rut = input(mensaje).strip()

    if not validar_rut(rut):
        print("Error: El RUT ingresado no es válido.")
        return None

    return normalizar_rut(rut)


def agregar_empleado():
    rut = leer_rut("Ingrese RUT del empleado: ")
    if rut is None:
        return
    nombre = input("Ingrese nombre del empleado: ")
    edad = leer_numero("Ingrese edad del empleado: ")
    
    print("Seleccione el cargo del empleado:")
    print("1.- Desarrollador")
    print("2.- Analista")
    print("3.- Jefe de Proyecto")
    print("4.- Soporte")
    print("5.- Otro")
    op_cargo = leer_numero("Seleccione opción: ")
    
    cargos = {1: "Desarrollador", 2: "Analista", 3: "Jefe de Proyecto", 4: "Soporte", 5: "Otro"}
    cargo = cargos.get(op_cargo, "Otro")
    
    sueldo = leer_flotante("Ingrese sueldo del empleado: ")

    try:
        emp = Empleado(rut, nombre, edad, cargo, sueldo)
    except (ValueError, TypeError) as e:
        print(f"Error de validación al crear el empleado: {e}")
        return

    conexion = db.conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO empleados (rut, nombre, edad, cargo, sueldo) VALUES (?, ?, ?, ?, ?)",
                           (emp.rut, emp.nombre, emp.edad, emp.cargo, emp.sueldo))
            conexion.commit()
            print("¡Empleado registrado exitosamente en la base de datos!")
        except sqlite3.IntegrityError:
            print("Error: Ya existe un empleado registrado con ese RUT.")
        except sqlite3.Error as e:
            print(f"Error en la base de datos: {e}")
        finally:
            conexion.close()

def buscar_empleado_db():
    rut = leer_rut("Ingrese RUT del empleado a buscar: ")
    if rut is None:
     return
    conexion = db.conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT rut, nombre, edad, cargo, sueldo FROM empleados WHERE rut = ?", (rut,))
            resultado = cursor.fetchone()
            if resultado:
                emp = Empleado(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4])
                print("-" * 30)
                print(emp)
                print("-" * 30)
                return emp
            else:
                print("No se encontró ningún empleado con ese RUT.")
                return None
        except sqlite3.Error as e:
            print(f"Error al consultar la base de datos: {e}")
        finally:
            conexion.close()
    return None


def convertir_sueldo_empleado():
    print("\n--- CONVERSIÓN DE SUELDO DE EMPLEADO ---")

    emp = buscar_empleado_db()

    if emp is None:
        return

    print(f"\nSueldo del empleado: ${emp.sueldo:,.0f} CLP")

    from monedas import convertir_monto

    convertir_monto(emp.sueldo)


def imprimir_todos():
    conexion = db.conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT rut, nombre, edad, cargo, sueldo FROM empleados")
            filas = cursor.fetchall()
            if not filas:
                print("No hay empleados registrados en el sistema.")
            else:
                print("--- LISTADO DE EMPLEADOS ---")
                for fila in filas:
                    emp = Empleado(fila[0], fila[1], fila[2], fila[3], fila[4])
                    print(emp)
                    print("-" * 20)
        except sqlite3.Error as e:
            print(f"Error al listar los empleados: {e}")
        finally:
            conexion.close()

def eliminar_empleado():
    rut = leer_rut("Ingrese RUT del empleado a eliminar: ")
    if rut is None:
        return
    conexion = db.conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT rut FROM empleados WHERE rut = ?", (rut,))
            if not cursor.fetchone():
                print("No se encontró el empleado para eliminar.")
                return
            
            cursor.execute("DELETE FROM empleados WHERE rut = ?", (rut,))
            conexion.commit()
            print("Empleado eliminado correctamente de la base de datos.")
        except sqlite3.Error as e:
            print(f"Error al eliminar: {e}")
        finally:
            conexion.close()

def editar_empleado():
    rut = leer_rut("Ingrese RUT del empleado a editar: ")
    if rut is None:
        return
    conexion = db.conectar()
    if not conexion:
        return
    
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT rut, nombre, edad, cargo, sueldo FROM empleados WHERE rut = ?", (rut,))
        resultado = cursor.fetchone()
        if not resultado:
            print("No se encontró el empleado.")
            conexion.close()
            return
        
        emp = Empleado(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4])
        print(emp)
        print("\nMenú de Edición:")
        print("1.- Cambiar nombre")
        print("2.- Cambiar edad")
        print("3.- Cambiar sueldo")
        op = leer_numero("Seleccione qué desea editar: ")
        
        if op == 1:
            nuevo_nombre = input("Ingrese nuevo nombre: ")
            emp.nombre = nuevo_nombre
            cursor.execute("UPDATE empleados SET nombre = ? WHERE rut = ?", (emp.nombre, rut))
        elif op == 2:
            nueva_edad = leer_numero("Ingrese nueva edad: ")
            emp.edad = nueva_edad
            cursor.execute("UPDATE empleados SET edad = ? WHERE rut = ?", (emp.edad, rut))
        elif op == 3:
            nuevo_sueldo = leer_flotante("Ingrese nuevo sueldo: ")
            emp.sueldo = nuevo_sueldo
            cursor.execute("UPDATE empleados SET sueldo = ? WHERE rut = ?", (emp.sueldo, rut))
        else:
            print("Opción de edición inválida.")
            conexion.close()
            return
        
        conexion.commit()
        print("¡Datos del empleado actualizados con éxito!")
    except (ValueError, TypeError, sqlite3.Error) as e:
        print(f"Error al actualizar el registro: {e}")
    finally:
        conexion.close()

def main():
    while True:
        opcion = menu()
        if opcion == 1:
            agregar_empleado()
        elif opcion == 2:
            buscar_empleado_db()
        elif opcion == 3:
            editar_empleado()
        elif opcion == 4:
            eliminar_empleado()
        elif opcion == 5:
            imprimir_todos()
        elif opcion == 6:
            mostrar_clima()
        elif opcion == 7:
            consultar_monedas()
        elif opcion == 8:
         convertir_sueldo()
        elif opcion == 9:
         convertir_sueldo_empleado()
        elif opcion == 0:
            print("Saliendo del sistema de EcoTech Solutions...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    if verificar_login():
        main()
    else:
        print("Acceso denegado.")
