"""
Decimal a Hexadecimal: Generar n números aleatorios entre el rango de 5000 y 450000, por cada uno de ellos
mostrar y generar el numero hexadecimal.
"""
from src.utils.validar import validar_si_es_numerico
import random

cantidad_numeros = int(validar_si_es_numerico("Cuantos numeros queres generar?"))

for num in range(cantidad_numeros):
    num_random = random.randint(5000, 450000)
    hexadecimal = hex(num_random)
    print(f"Entero: {num_random} - Hexadecimal: {hexadecimal}")