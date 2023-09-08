# Escribir un programa que pida dos números y muestre como resultado su división, cociente y resto.
from src.utils.validar import validar_si_es_numerico

# Se solicita los numeros
numero1 = float(validar_si_es_numerico("Ingrese el primer número: "))
numero2 = float(validar_si_es_numerico("Ingrese el segundo número: "))

# Calcular la división, cociente y resto
division = numero1 / numero2
cociente = numero1 // numero2
resto = numero1 % numero2

# Mostrar los resultados
print("Resultado de la división:", division)
print("Cociente:", cociente)
print("Resto:", resto)