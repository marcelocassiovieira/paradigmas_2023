"""
Suma - División - Potencia. Se necesita desarrollar un programa que permita calcular la suma de tres números.
Si el resultado es mayor a 10 dividir por 2 (mostrar su resultado sin decimales),
en caso contrario elevar el resultado al cubo.
"""
from src.utils.validar import validar_si_es_numerico

# Ingreso de los numeros
numero1 = float(validar_si_es_numerico("Ingrese el numero 1:"))
numero2 = float(validar_si_es_numerico("Ingrese el numero 2:"))
numero3 = float(validar_si_es_numerico("Ingrese el numero 2:"))

# Suma de los numeros
resultado = numero1 + numero2 + numero3

# Evalua, calcula e imprime el resultado
if resultado > 10:
    print(int(resultado / 2))
else:
    print(int(resultado**3))



