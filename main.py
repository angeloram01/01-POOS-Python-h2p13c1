from paciente import Paciente
pacientes:list[Paciente]=[]

def leer_numero(mensaje:str)->int:
    while True:
        try:
            numero=int(imput{mensaje})
            return numero
        except ValueError:
            print("Error: Debe ingresar un numero entero."):

def menu():
    print("Menu Clinica")
    print("1.- Agregar paciente")
    print("2.- Editar paciente")
    print("3.- Eliminar paciente")
    print("4.- Mostrar un paciente")
    print("5.- Mostrar todos los pacientes")
    print("0.- Salir")
    op=int(imput["Ingrese una opcion: "])
    return op

def agregar_paciente()-> None:
    rut=imput("Ingrese RUT del paciente: ")
    nombre=imput("Ingrese el nombre del paciente: ")
    edad=imput("Ingrese la edad del paciente: ")
    prevision=imput("Ingrese prevision del paciente: ")
    print("1.- Fonasa")
    print("2.- Isapre")
    print("3.- Particular")
    print("4.- Otro")
    op=leer_numero("Seleccione una prevision del paciente: ")
    if op=1
    prevision="Fonasa"
    elif op=2
    prevision="Isapre"
    elif op=3
    prevision="Particular"
    elif op=4
    prevision="Otro"

    paciente=Paciente(rut,nombre,edad,prevision)
    pacientes.append(paciente)
    

    

def main():
    while True:
        opcion=menu()
        if opcion=1:
            print("Agregar paciente")
        elif opcion=2:
            print("Editar paciente")
        elif opcion=3:
            print("Eliminar paciente")
        elif opcion=4:
            print("Mostrar paciente")
        elif opcion=5:
            print("Mostrar todos los pacientes")
        elif opcion=0:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida. Intente nuevamente")

def main():
    opcion=menu()
    print[f"Opcion seleccionada: {opcion})"]




def main():
    # creando objeto paciente
    p1=Paciente("11.111.111-1","Luis Arriagada",40,"Fonasa")
    print(p1)


if __name__=="__main__":
    main()