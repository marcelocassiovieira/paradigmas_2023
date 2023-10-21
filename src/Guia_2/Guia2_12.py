"""
Números pares e impares
Se pide desarrollar un programa que permita leer una serie de números.
La finalización de carga de datos se presenta cuando el usuario ingrese un número negativo.
Los requerimientos funcionales del programa son:
La sumatoria de solo los números que estén comprendidos entre 50 y 100.
Cantidad de valores pares ingresados.
Cantidad de valores impares ingresados.
Informar si en la carga de números se ingreso al menos un número 0.
Informar si la serie contiene solo números pares e impares alternados.
"""

numeros_sumatoria = 0
cant_valores_pares = 0
cant_valores_impares = 0
ingreso_cero = False
pares_impares_alternados = False
flag = True
anterior = None
anterior_flag = True

while flag:
    numero_input = int(input("Ingrese un numero: "))

    if numero_input < 0:
        flag = False
        break

    if anterior_flag:
        anterior = numero_input
        anterior_flag = False

    if 50 <= numero_input <= 100:
        numeros_sumatoria += numero_input

    if numero_input % 2 == 0:
        cant_valores_pares += 1
    else:
        cant_valores_impares += 1

    if numero_input == 0:
        ingreso_cero += 1

    if anterior % 2 == 0 and numero_input % 2 != 0 or anterior % 2 != 0 and numero_input % 2 == 0:
        pares_impares_alternados = True

    anterior = numero_input


print(f"Sumatoria: {numeros_sumatoria}")
print(f"Pares: {cant_valores_pares}")
print(f"Impares: {cant_valores_impares}")

if ingreso_cero > 0:
    print("Hay al menos un numero 0")

if pares_impares_alternados:
    print("Hay pares impares alternados")