"""
Búsqueda de mayor
Realizar un programa que permita buscar el mayor de 10.000 números aleatorios generados en el rango de[0,100.000].
"""

import random

MIN_NUM = 0
MAX_NUM = 100000
flag = True


for num in range(0, 10000):
    num_aleatorio = random.randint(MIN_NUM, MAX_NUM)
    if flag:
        mayor = num_aleatorio
        flag = False
    if num_aleatorio > mayor:
        mayor = num_aleatorio

print("Mayor: " + str(mayor))
