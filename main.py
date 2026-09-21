from paciente import Paciente
pacientes:list[Paciente] = []


def leer_numero(mensaje:str)->int:
    while True:
        try:
            numero=int(input(mensaje))
            return numero
        except ValueError:
            print("Error: debe ingresar un número entero. intente nuevamente.")


def menu(): 
    print("="*25)
    #Opción menú CRUD.
    print("Menú Clínica:")
    print("1.- Agregar paciente")
    print("2.- Editar paciente")
    print("3.- Eliminar paciente")
    print("4.- Mostrar paciente")
    print("5.- Mostrar todos los pacientes")
    print("0.- Salir") #Dar opción de salir del programa.
    op= leer_numero("Ingrese una opción: ")
    print("="*25)
    return op


def agregar_paciente()->None:
    rut=input("Ingrese el RUT del paciente: ")
    nombre=input("Ingrese el nombre del paciente:")
    edad=leer_numero("Ingrese la edad del paciente:")
    print("Tipo de previsión del paciente:")
    print("1.- Fonasa")
    print("2.- Isapre")
    print("3.- Particular")
    print("4.- Otro")
    op=leer_numero("Ingrese una opción: ")
    if op==1:
        prevision="Fonasa"
    elif op==2:
        prevision="Isapre"
    elif op==3:
        prevision="Particular"
    elif op==4:
        prevision="Otro"
    else:
        print("Opción inválida. Por favor ingrese alguna de las opciones mostradas anteriormente.")
    paciente=Paciente(rut,nombre,edad,prevision)
    pacientes.append(paciente)
    print("Paciente agregado exitosamente.")
    print(f"Total de pacientes registrados: {len(pacientes)}")
    

def main():
   while True:
        opcion=menu()
        if opcion==1:
            print("Agregar paciente")
            agregar_paciente()
        elif opcion==2:
            print("Editar paciente")
        elif opcion==3:
            print("Eliminar paciente")
        elif opcion==4:
            print("Mostrar paciente")
        elif opcion==5:
            print("Mostrar todos los pacientes")
        elif opcion==0:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__=="__main__":
    main()