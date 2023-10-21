from src.Integrador.Socio import Socio
from datetime import datetime


listado_socios = {
    1: Socio("1", "Amanda", "Nunez", datetime(2009, 3, 17), False),
    2: Socio("2", "Bárbara", "Molina", datetime(2009, 3, 17), False),
    3: Socio("3", "Lautaro", "Campos", datetime(2009, 3, 17), False),
    4: Socio("4", "Michael", "Johnson", datetime(2018, 3, 13), True),
    5: Socio("5", "Jessica", "Brown", datetime(2018, 3, 13), True),
    6: Socio("6", "David", "Davis", datetime(2023, 10, 14), False),
    7: Socio("7", "Sarah", "Taylor", datetime(2023, 10, 13), False),
    8: Socio("8", "Christopher", "Wilson", datetime(2018, 3, 13), True),
    9: Socio("9", "Michelle", "Anderson", datetime(2018, 3, 13), True),
    10: Socio("10", "James", "Harris", datetime(2023, 10, 11), False)
}


def menu():
    print("--------------------------------")
    print("1 - Informar cantidad de socios.")
    print("2 - Verificar cuota al dia.")
    print("3 - Modificar fechas de ingreso.")
    print("4 - Eliminar socio por nombre y apellido.")
    print("5 - Imprimir listado de socios.")
    print("6 - Salir")
    return input("Seleccione una opcion:")


def return_cantidad_socios():
    print(f"Cantidad de socios: {len(listado_socios)} socios.")


def verificar_cuota_al_dia():
    numero_socio = input("Ingrese el numero de socio:")
    for clave, socio in listado_socios.items():
        if socio.numero == numero_socio:
            pago = input("Pago todas las cuotas? s/n")
            if pago == "s":
                socio.cuota_al_dia = True
            elif pago == "n":
                socio.cuota_al_dia = False
            else:
                print("Opcion invalida, se cancela el procesamiento")
            break


def modificar_fechas_ingreso():
    # fecha_str = input("Ingrese la fecha en formato dd/mm/yyyy: ")
    # try:
    #     fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
    #     print("Fecha ingresada:", fecha)
    # except ValueError:
    #     print("El formato de fecha ingresado es incorrecto.")

    fecha_anterior = datetime(2018, 3, 13)
    fecha_nueva = datetime(2018, 3, 14)
    for clave, socio in listado_socios.items():
        if socio.fecha_ingreso == fecha_anterior:
            socio.fecha_ingreso = fecha_nueva


def eliminar_socio():
    nombre = input("Ingrese el nombre del socio: ")
    apellido = input("Ingrese apellido del socio: ")
    socio_eliminado = False
    for clave, socio in listado_socios.items():
        if socio.nombre == nombre and socio.apellido == apellido:
            del listado_socios[clave]
            socio_eliminado = True
            break
    if socio_eliminado:
        print("Socio eliminado...")
    else:
        print("Socio no encontrado...")


def imprimir_listado_socios():
    for clave, socio in listado_socios.items():
        print(f"Numero: {socio.numero}")
        print(f"Nombre: {socio.nombre}")
        print(f"Apellido: {socio.apellido}")
        print(f"Fecha Ingreso: {socio.fecha_ingreso}")
        print(f"Cuota al dia: {'Si' if socio.cuota_al_dia else 'No'}")
        print("*************************************")


def inicializar():
    print("Menu: ")
    while True:
        opcion = menu()
        if opcion == '1':
            return_cantidad_socios()
        elif opcion == '2':
            verificar_cuota_al_dia()
        elif opcion == '3':
            modificar_fechas_ingreso()
        elif opcion == '4':
            eliminar_socio()
        elif opcion == '5':
            imprimir_listado_socios()
        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opcion invalida...")

    print(opcion)


inicializar()
