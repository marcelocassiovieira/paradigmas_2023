"""
Menores y promedio
Realizar un programa que genere 5000 numeros aleatorios en el rango de [0,100000] y que permita:
Determinar el menor de los numeros genera dos en forma aleatoria.
Calcular el valor promedio de los números menores a 10.000.
"""

import random


acum_menor = 0
cant_menores = 0
MIN_NUM = 0
MAX_NUM = 100000
flag_menor = True

for num in range(0, 5000):
    num_aleatorio = random.randint(MIN_NUM, MAX_NUM)
    if flag_menor:
        menor = num_aleatorio
        flag_menor = False

    if num_aleatorio < menor:
        menor = num_aleatorio
        cant_menores += 1

    if num_aleatorio < 10000:
        acum_menor += num_aleatorio

promedio = acum_menor / cant_menores

print(f"Menor valor: {menor}")
print(f"Primedio menores a 10000: {promedio}")