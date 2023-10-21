"""
Menu de Opciones con secuencias. Escribir un programa que le permita al usuario, a través de un menú de opciones,
las siguientes operaciones:
a) Generar una serie n de números (n ingresado por teclado y validando que sea mayor a cero) y mostrar la suma de los cuadrados
b) Ingresar un texto finalizado por un punto y determinar la cantidad de palabras que finalizan con vocales
c) Ingresar una serie de números (la carga finaliza con cero) y determinar si hay mayor cantidad de valores pares o de impares
d) Salir
"""

from src.utils.validar import es_numero
from src.utils.validar import es_mayor_que_cero
from src.utils.validar import validar_si_es_numerico


def suma_cuadrados():
    numeros = []
    invalido = True

    while invalido:
        numero = input("Ingrese un numero para continuar, para salir, cualquier otro digito:")
        if es_numero(numero):
            numero = int(numero)
            if es_mayor_que_cero(numero):
                numeros.append(numero)
            else:
                print("Debe ser mayor a cero...")
        else:
            invalido = False

    suma = 0
    for numero in numeros:
        suma += numero * numero

    print(f"Suma de los cuadrados de los numeros ingresados:{suma}")


def contador_vocales():
    cont_vocales = 0
    vocales = ["a", "e", "i", "o", "u"]
    texto = input("Ingrese el texto que termine con un punto(.).")
    lista_caracteres = list(texto.lower())
    for caracter in lista_caracteres:
        if caracter in vocales:
            cont_vocales += 1
    print(f"Cantidad de vocales: {cont_vocales}")


def pares_impares():
    pares = 0
    impares = 0

    while True:
        numero = int(validar_si_es_numerico("Ingrese un numero. 0 para salir:"))
        if numero == 0:
            print("Saliendo...")
            break
        else:
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1

    print(f"Numeros pares:{pares}")
    print(f"Numeros impares: {impares}")


def menu():
    print("Menu de Opciones con secuencias.")
    print("------------------------------------")
    print("1. Generar una serie n de números y mostrar la suma de los cuadrados.")
    print(
        "2. Ingresar un texto finalizado por un punto y determinar la cantidad de palabras que finalizan con vocales.")
    print("3. Ingresar una serie de números  y determinar si hay mayor cantidad de valores pares o de impares.")
    print("4. Salir.")


########################################################################################################################

menu()

while True:
    opcion = input("Elige una opcion: ")
    if opcion == '1':
        suma_cuadrados()
    elif opcion == '2':
        contador_vocales()
    elif opcion == '3':
        pares_impares()
    elif opcion == '4':
        print("Saliendo...")
        break
    else:
        print("Opción inválida. Por favor, elige una opción válida.")

