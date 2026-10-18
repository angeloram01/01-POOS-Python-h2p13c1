from paciente import Paciente
import database

def leer_numero(mensaje:str)->int:
    while True:
        try:
            numero=int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Debe ingresar un número entero.")

def menu():
    print("="*20)
    print("Menú Clínica")
    print("="*20)
    print("1.- Agregar paciente")
    print("2.- Editar paciente")
    print("3.- Eliminar paciente")
    print("4.- Mostrar un paciente")
    print("5.- Mostrar todos los pacientes")
    print("0.- Salir")
    op=leer_numero("Ingrese una opción: ")
    print("="*20)
    return op

def agregar_paciente()-> None:
    rut=input("Ingrese RUT del paciente: ")
    nombre=input("Ingrese nombre del paciente: ")
    edad=leer_numero("Ingrese edad del paciente: ")
    print("Tipo de previsión del paciente: ")
    print("1.- Fonasa")
    print("2.- Isapre")
    print("3.- Particular")
    print("4.- Otro ")
    op=leer_numero("Seleccione una previsión del paciente: ")
    if op==1:
        prevision="Fonasa"
    elif op==2:
        prevision="Isapre"
    elif op==3:
        prevision="Particular"
    elif op==4:
        prevision="Otro"
    else:
        prevision=""

    try:
        paciente = Paciente(rut, nombre, edad, prevision)
        database.insertar_paciente(paciente)  # Guardar en base de datos
        print("Paciente agregado exitosamente a la base de datos.")
    except (ValueError,TypeError) as e:
        print(f"Error al crear el paciente: {e}")

def imprimir_pacientes()->None:
    pacientes = database.obtener_todos_los_pacientes()
    if len(pacientes) == 0:
        print("No hay pacientes registrados.")
    else:
        for paciente in pacientes:
            print(paciente)
            print("-"*20)

def buscar_paciente()->Paciente | None:
    rut = input("Ingrese RUT del paciente: ")
    return database.buscar_paciente_por_rut(rut)

def imprimir_paciente()->None:
    paciente = buscar_paciente()
    if paciente:
        print(paciente)
    else:
        print("No se encontró el paciente.")

def eliminar_paciente()->None:
    paciente = buscar_paciente()
    if paciente:
        database.eliminar_paciente_db(paciente.rut)
        print("Paciente eliminado de la base de datos.")
    else:
        print("No se encontró el paciente.")

def editar_paciente()->None:
    paciente = buscar_paciente()
    if paciente:
        print(paciente)
        print("Menú de edición")
        print("1.- Editar nombre")
        print("2.- Editar edad")
        print("3.- Editar previsión")
        print("0.- Salir")
        op = leer_numero("Ingrese una opción: ")
        
        if op == 1:
            nombre_nuevo = input("Ingrese nuevo nombre: ")
            try:
                paciente.nombre = nombre_nuevo
            except ValueError as e:
                print(f"Error al actualizar el nombre: {e}")
                return
            print("Nombre actualizado")
            
        elif op == 2:
            edad_nueva = leer_numero("Ingrese nueva edad: ")
            try:
                paciente.edad = edad_nueva
            except (ValueError, TypeError) as e:
                print(f"Error al actualizar la edad: {e}")
                return
            print("Edad actualizada")
            
        elif op == 3:
            print("Tipos de previsión: ")
            print("1.- Fonasa")
            print("2.- Isapre")
            print("3.- Particular")
            print("4.- Otro")
            op_prev = leer_numero("Seleccione una previsión: ")        
            try:
                if op_prev == 1:
                    paciente.prevision = "Fonasa"
                elif op_prev == 2:
                    paciente.prevision = "Isapre"
                elif op_prev == 3:
                    paciente.prevision = "Particular"
                elif op_prev == 4:
                    paciente.prevision = "Otro"
                else:
                    print("Opción inválida")
                    return
                print("Previsión actualizada")
            except (ValueError, TypeError) as e:
                print(f"Error al actualizar la previsión: {e}")
                return

        # Guardar los cambios actualizados en la base de datos
        database.insertar_paciente(paciente)
        print("Cambios guardados exitosamente en la base de datos.")
    else:
        print("No se encontró el paciente.")

def main():
    # Inicializar la base de datos al arrancar
    database.inicializar_base_datos()

    while True:
        opcion = menu()
        if opcion == 1:
            agregar_paciente()
        elif opcion == 2:
            editar_paciente()
        elif opcion == 3:
            eliminar_paciente()
        elif opcion == 4:
            imprimir_paciente()
        elif opcion == 5:
            imprimir_pacientes()
        elif opcion == 0:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()