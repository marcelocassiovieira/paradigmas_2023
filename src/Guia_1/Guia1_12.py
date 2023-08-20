# Ahorros. Escribir un programa en el cual muestre a fin de año el total de ahorro obtenido,
# si se pide en cada mes el 10% del sueldo ganado.

# Se ingresa el valor a depositar
ahorro = float(input("Ingrese cuanto queres ahorrar: "))
PORCENTAGE_INTERES_MENSUAL = 10

# Se calcula el interes compuesto
for num in range(1, 13):
    ahorro += ahorro * PORCENTAGE_INTERES_MENSUAL / 100

# Se imprime el resultado
print(ahorro)