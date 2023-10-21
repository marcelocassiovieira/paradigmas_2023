"""
Promedio de números aleatorios: Realice un programa que permita calcular el promedio de 1000 números aleatorios
generados en el rango de[0,100000].
"""
import random

MIN_NUM = 0
MAX_NUM = 100000
total = 0

for num in range(0, 1000):
    num_aleatorio = random.randint(MIN_NUM, MAX_NUM)
    total += num_aleatorio

print(f"Promedio: {total / MAX_NUM}")
