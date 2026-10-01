from paciente import Paciente
pacientes:list[Paciente]=[
        Paciente("11.111.111-1","Juan Perez",30,"Fonasa"),
        Paciente("22.222.222-2","Maria Gonzalez",25,"Isapre")
    ]

def leer_numero(mensaje:str)->int:
    while True:
        try:
            numero=int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Debe ingresar un número entero.")

def menu_principal():
    print("="*20)
    print("Menú Principal")
    print("="*20)
    print("1.- Menú Pacientes")
    print("2.- Menú Departamentos")
    print("3.- Salir")
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

    try:
        paciente=Paciente(rut,nombre,edad,prevision)
    except (ValueError, TypeError) as e:
        print(f"Error al crear el paciente: {e}")
        return
    pacientes.append(paciente)  
    print("Paciente agregado exitosamente.")
    print(f"Total de pacientes: {len(pacientes)}")

def imprimir_pacientes()->None:
    if len(pacientes)==0:
        print("No hay pacientes")
    else:
        for paciente in pacientes:
            print(paciente)
            print("-"*20)

def buscar_paciente()->Paciente:
    rut=input("Ingrese RUT del paciente: ")
    for p in pacientes:
        if p.rut==rut:
            return p
    return None

def imprimir_paciente()->None:
    paciente=buscar_paciente()
    if paciente:
        print(paciente)
    else:
        print("No se encontró el paciente.")

def eliminar_paciente()->None:
    paciente=buscar_paciente()
    if paciente:
        pacientes.remove(paciente)
        print("Paciente eliminado")
    else:
        print("No se encontró el paciente.")

def editar_paciente()->None:
    paciente=buscar_paciente()
    if paciente:
        print(paciente)
        print("Menú de edición")
        print("1.- Editar nombre")
        print("2.- Editar edad")
        print("3.- Editar previsión")
        print("0.- Salir")
        op=leer_numero("Ingrese una opción: ")
        try:
            if op==1:
                nombre_nuevo=input("Ingrese nuevo nombre: ")
                try:
                    paciente.nombre=nombre_nuevo
                except (ValueError) as e:
                    return
                print("Nombre actualizado")
            elif op==2:
                edad_nueva=leer_numero("Ingrese nueva edad: ")
                paciente.edad=edad_nueva
                print("Edad actualizada")
            elif op==3:
                print("Tipos de previsión: ")
                print("1.- Fonasa")
                print("2.- Isapre")
                print("3.- Particular")
                print("4.- Otro")
                op=leer_numero("Seleccione una previsión: ")
                if op==1:
                    paciente.prevision="Fonasa"
                    print("Previsión actualizada")
                elif op==2:
                    paciente.prevision="Isapre"
                    print("Previsión actualizada")
                elif op==3:
                    paciente.prevision="Particular"
                    print("Previsión actualizada")
                elif op==4:
                    paciente.prevision="Otro"
                    print("Previsión actualizada")
        except (ValueError, TypeError) as e:
                print(f"Error al actualizar la previsión {e}")
                
        else:
                print("Opción inválida")
    else:
            print("No se encontró el paciente.")

def menu_paciente():
    print("="*20)
    print("Menú Clínica")
    print("="*20)
    print("1.- Agregar paciente")
    print("2.- Editar paciente")
    print("3.- Eliminar paciente")
    print("4.- Mostrar un paciente")
    print("5.- Mostrar todos los pacientes")
    print("0.- Salir")
    op == leer_numero("Ingrese una opción")
    try:
        if op == 1:
            agregar_paciente()
        elif op == 2:
            editar_paciente()
    except:
        
  

from departamento import Departamento

departamentos:list[Departamento]=[
        Departamento( 1,"José Soto",3),
        Departamento(2,"Sofía Perez",1)
    ]

def menu_depto():
    print("="*20)
    print("Menú Departamento")
    print("="*20)
    print("1.- Agregar departamento")
    print("2.- Editar departamento")
    print("3.- Eliminar departamento")
    print("4.- Mostrar departamentos")
    print("5.- Mostrar todos los departamentos")
    print("0.- Salir")
    op=leer_numero("Ingrese una opción: ")
    print("="*20)
    return op

def agregar_depto()-> None:
    id_departamento=input("Ingrese el ID del departamento: ")
    nombre=input("Ingrese el nombre del departamento: ")
    piso=input("Ingrese el número de piso: ")

    departamento=Departamento(id_departamento,nombre, piso)
    departamentos.append(departamento)  
    print("Departamento agregado exitosamente.")
    print(f"Total de departamentos: {len(departamentos)}")

def imprimir_deptos()->None:
    if len(departamento)==0:
        print("No hay departamentos")
    else:
        for departamento in departamentos:
            print(departamento)
            print("-"*20)


def buscar_deptos()->Departamento:
    id_departamento=input("Ingrese ID del departamento: ")
    for d in departamentos:
        if d.id_departamento==id_departamento:
            return d
    return None


def imprimir_depto()->None:
    departamento=buscar_deptos()
    if departamento:
        print(departamento)
    else:
        print("No se encontró el departamento.")

def eliminar_depto()->None:
    departamentos=buscar_deptos()
    if departamentos:
        departamentos.remove(departamentos)
        print("Departamento eliminado")
    else:
        print("No se encontró el departamento.")


def main():

    while True:
        print("="*20)
        print("Menú Principal")
        print("="*20)
        print("1.- Menú Pacientes")
        print("2.- Menú Departamentos")
        print("3.- Salir")
        op=leer_numero("Ingrese una opción: ")
        print("="*20)

        if op == 1:
            menu_paciente()
        elif op == 2:
            menu_depto()
        elif op == 3:
            break

if __name__=="__main__":
    main()

