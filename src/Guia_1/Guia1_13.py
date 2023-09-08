# Crear un conversor de pies y pulgadas a centímetros.

from src.utils.validar import validar_si_es_numerico
from src.utils.validar import validar_opciones_correctas

# Se solicita el tipo de conversion
print("Seleccione una opción:")
print("1. Convertir pies a centimetros")
print("2. Convertir pulgadas a centimetros")
opciones = [1, 2]

opcion = int(validar_opciones_correctas("Ingrese el número de la opción deseada: ", opciones))

# Se solicita la cantidad
cantidad = int(validar_si_es_numerico("Ingresa la cantidad: "))

# Declaro las constantes de equivalencia
PIE_A_CENTIMETRO = 30.48
PULGADA_A_CENTIMETRO = 2.54

# Formato del texto
texto_singular_o_plural = ("s" if cantidad > 1 else "")

# Se calcula en base a la opcion y se imprime
if opcion == 1:
    resultado = cantidad * PIE_A_CENTIMETRO
    print(f"{cantidad} pie{texto_singular_o_plural} corresponden a {resultado} centimetros")

if opcion == 2:
    resultado = cantidad * PULGADA_A_CENTIMETRO
    print(f"{cantidad} pulgada{texto_singular_o_plural} corresponden a {resultado} centimetros")

