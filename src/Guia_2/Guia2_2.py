"""
Secuencia de impares. Cargar por teclado dos números, e imprimir los números impares que se encuentran comprendidos
entre ellos, en forma ascendente y descendente.
"""
from src.utils.validar import validar_si_es_numerico

primer_numero = int(validar_si_es_numerico("Ingrese primer numero: "))
segundo_numero = int(validar_si_es_numerico("Ingrese segundo numero: "))

for numero in range(primer_numero, segundo_numero + 1):
    if numero % 2 != 0:
        print(numero)
