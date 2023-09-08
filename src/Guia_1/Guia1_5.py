"""
Area de un triángulo. Desarrolle un programa para calcular el área de un triángulo,
cargando por teclado el valor de la base, pero sabiendo que su altura es igual al cuadrado de la base.
"""
from src.utils.validar import validar_si_es_numerico

# Se ingresa el valor de la base
base = float(validar_si_es_numerico("Ingrese el valor de la base: "))

# Se asigna el valor de la altura que es el cuadrado de la base
altura = base**2

# Se calcula el area del triangulo
resultado = (base * altura) / 2

# Se imprime el resultado
print(f"El area del triangulo es: {resultado}")