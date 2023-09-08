# Crear un conversor de dólares a pesos y pesos a dólares, donde se ingrese por teclado el valor del peso actual.

from src.utils.validar import validar_si_es_numerico
from src.utils.validar import validar_opciones_correctas

valor_peso = float(validar_si_es_numerico("Ingrese el valor actual del peso: "))

print("Seleccione una opción:")
print("1. Convertir de dólares a pesos")
print("2. Convertir de pesos a dólares")
opciones = [1, 2]

opcion = int(validar_opciones_correctas("Ingrese el número de la opción deseada: ", opciones))

if opcion == 1:
    dolares = float(validar_si_es_numerico("Ingrese el la cantidad de dolares: "))
    resultado = dolares * valor_peso
    print(f"{dolares} dolares equivalen a {resultado} pesos.")

if opcion == 2:
    pesos = float(validar_si_es_numerico("Ingrese el la cantidad de pesos: "))
    resultado = pesos / valor_peso
    print(f"{pesos} pesos equivalen a {resultado} dolares.")


