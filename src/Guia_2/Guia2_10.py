"""
Menores y promedio
Realizar un programa que genere 5000 numeros aleatorios en el rango de [0,100000] y que permita:
Determinar el menor de los numeros generados en forma aleatoria.
Calcular el valor promedio de los números menores a 10.000.
"""

import random

MIN_NUM = 0
MAX_NUM = 100000
flag = True
acum_menores = 0
cont_menores = 0

for num in range(0, 5000):
    num_aleatorio = random.randint(MIN_NUM, MAX_NUM)
    if flag:
        menor = num_aleatorio
        flag = False
    if num_aleatorio < menor:
        menor = num_aleatorio

    if num_aleatorio < 10000:
        acum_menores += num_aleatorio
        cont_menores += 1

print("Mayor: " + str(menor))
print(f"Promedio numeros menores: {(acum_menores / cont_menores)}")