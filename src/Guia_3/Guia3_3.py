"""
Secuencia numérica. Ingresar una secuencia de números, de a uno por vez, la carga finaliza cuando el usuario ingresa el cero.
Determinar:
a) Porcentaje que representan los números divisibles por 3 sobre el total de números ingresados en la secuencia
b) Determinar la cantidad de números que son el cuadrado del número anterior
c) Determinar la posición del mayor elemento impar de la secuencia
"""


def empezar_programa():
    cargar_numeros()


def multiples_de_tres(numeros):
    cont_multiples_tres = 0
    for numero in numeros:
        if numero % 3 == 0:
            cont_multiples_tres += 1

    return cont_multiples_tres


def cuadrado_numero_anterior(numeros):
    num_anterior = None
    cont_cuadrados = 0
    for numero in numeros:
        if num_anterior is None:
            num_anterior = numero
        else:
            cuadrado = num_anterior * num_anterior
            if cuadrado == numero:
                cont_cuadrados += 1
            num_anterior = numero

    return cont_cuadrados


def determinar_impar_mayor(numeros):
    impar_mayor = None
    for numero in numeros:
        if numero % 2 > 0:
            if impar_mayor is None:
                impar_mayor = numero
            if numero > impar_mayor:
                impar_mayor = numero

    return impar_mayor


def cargar_numeros():
    numeros = []
    while True:
        numero = input("Ingrese el numero:")
        if numero.isnumeric():
            numero = int(numero)
            if numero == 0:
                break
            else:
                numeros.append(numero)
        else:
            print("Debe ser numerico!")

    multiples = multiples_de_tres(numeros)
    cuadrados = cuadrado_numero_anterior(numeros)
    impar = determinar_impar_mayor(numeros)

    print(f"Cantidad de multiples de 3: {multiples}")
    print(f"Cantidad de cuadrados iguales:{cuadrados}")
    print(f"Impar mayor: {impar}")


empezar_programa()
