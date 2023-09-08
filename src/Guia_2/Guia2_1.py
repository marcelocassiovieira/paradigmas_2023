"""
Ciclistas: La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado). Desarrollar un programa
que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:
a) Determinar y mostrar el nombre del ganador de la carrera.
b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del ganador es menor al
tiempo record, mostrar un mensaje.
c) Calcular y mostrar el tiempo promedio entre todos los ciclistas.
"""

from src.utils.validar import validar_si_es_numerico

resultados_competidores = {}
texto_si_supero_record = ""
INDEX_TIEMPO = 1

tiempo_record = float(validar_si_es_numerico("Ingrese el tiempo record: "))

cant_competidores = int(validar_si_es_numerico("Ingrese la cantidad de competidores: "))

print(cant_competidores)
#
for competidor in range(cant_competidores):
    nombre = input("Ingrese nombre del ciclista: ")
    tiempo_carrera = float(validar_si_es_numerico("Ingrese el tiempo de carrera: "))
    resultados_competidores[nombre] = tiempo_carrera

menor_tiempo = next(iter(resultados_competidores.items()))[INDEX_TIEMPO]

ganador = next(iter(resultados_competidores.items()))

for nombre, tiempo in resultados_competidores.items():
    if tiempo < menor_tiempo:
        menor_tiempo = tiempo
        ganador = (nombre, tiempo)

if(not ganador[1] < tiempo_record):
    texto_si_supero_record = "no"

print("*********************************************************************")
print(f"Ganador: {ganador[0]} con {ganador[1]} segundos.")
print(f"{ganador[0]}{texto_si_supero_record} superó el record de {tiempo_record} segundos")
print(f"El promedio de tiempo en la competicion fue de: {sum(resultados_competidores.values()) / len(resultados_competidores)} segundos.")
