# Crear un conversor de dólares a pesos y pesos a dólares, donde se ingrese por teclado el valor del peso actual.

valor_peso = float(input("Ingrese el valor actual del peso: "))

print("Seleccione una opción:")
print("1. Convertir de dólares a pesos")
print("2. Convertir de pesos a dólares")
opcion = int(input("Ingrese el número de la opción deseada: "))

if opcion == 1:
    dolares = float(input("Ingrese el la cantidad de dolares: "))
    resultado = dolares * valor_peso
    print(f"{dolares} dolares equivalen a {resultado} pesos.")

if opcion == 2:
    pesos = float(input("Ingrese el la cantidad de pesos: "))
    resultado = pesos / valor_peso
    print(f"{pesos} pesos equivalen a {resultado} dolares.")


