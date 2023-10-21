from collections import Counter

lista_enteros = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8]


def encontrar_elemento_no_repetido(arreglo):
    elementos_repetidos = set()
    elementos_unicos = set()

    for numero in lista_enteros:
        if numero not in elementos_unicos:
            elementos_unicos.add(numero)
        else:
            elementos_repetidos.add(numero)

    elementos_no_repetido = elementos_unicos - elementos_repetidos

    print(elementos_no_repetido)


def encontrar_elemento_no_repetido_2(arreglo):
    elementos_unicos = []
    contador_repetidos = 0
    for numero in arreglo:
        for num in arreglo:
            if num == numero:
                contador_repetidos += 1
        if contador_repetidos == 1:
            elementos_unicos.append(num)
        contador_repetidos = 0
    print(elementos_unicos)


def encontrar_elemento_no_repetido_3(arreglo):
    counter = Counter(arreglo)
    lista_unicos = []
    for num, frec in counter.items():
        if frec == 1:
            lista_unicos = [num]

    print(lista_unicos)


def encontrar_elemento_no_repetido_4(arreglo):
    numero = 2 * sum(set(arreglo)) - sum(arreglo)
    print(numero)


encontrar_elemento_no_repetido_4(lista_enteros)
