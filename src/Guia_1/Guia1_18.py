"""
Tarjeta de Bingo. Realizar un programa que genere 15 números aleatorios enteros en el rango del 1 al 100,
que representaría la tarjeta de bingo de una persona. Una vez generado los números aleatorios solicitar
al usuario que ingrese 3 números enteros, a parƟr de allí mostrar los siguientes mensajes:
Si el usuario no marcó ninguno de los números, indicarlo diciendo “El jugador tiene mala suerte,
no marcó ninguna casilla”. Caso contrario mostrar “El jugador marcó algún número de la tarjeta”
"""
import random

# Defino variables, constantes y arreglos
TAMANO_TARJETA = 15
cant_aciertos = 0
numeros_jugador = []
tarjeta = []


# Genero los numeros aleatorios, si no existe en la tarjeta se agrega
while len(tarjeta) < TAMANO_TARJETA:
    numero_aleatorio = random.randint(1, 15)
    if numero_aleatorio not in tarjeta:
        tarjeta.append(numero_aleatorio)

# Se ordena los numeros de la tarjeta en orden ascendente
tarjeta.sort()

# Se ingresa los numeros de los jugadores y se los agrega a la lista de numeros del jugador
numeros_jugador.append(int(input("Ingrese el primer numero: ")))
numeros_jugador.append(int(input("Ingrese el segundo numero: ")))
numeros_jugador.append(int(input("Ingrese el tercer numero: ")))

# Se evalua cuantos numeros acerto el jugar
for num in numeros_jugador:
    if num in tarjeta:
        cant_aciertos += 1

# Se imprime los resultados
print("El jugador tiene mala suerte, no marcó ninguna casilla" if cant_aciertos == 0 else "El jugador marcó algún número de la tarjeta")
