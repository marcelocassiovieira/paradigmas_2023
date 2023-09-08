"""
Conversión de medidas. Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en:
yardas pulgadas cenơmetros metros Sabiendo que: 1 pie = 12 pulgadas 1 yarda = 3 pies 1 pulgada = 2.54 centímetros 1 metro = 1000
"""
from src.utils.validar import validar_si_es_numerico

# Se solicita el ingreso por teclado
cantidad_pies = int(validar_si_es_numerico("Ingrese la cantidad de pies para la conversion:"))

# Se define constantes de conversiones
PIE_A_PULGADAS = 12
YARDA_A_PIE = 3
PULGADA_A_CENTIMETROS = 2.54
METRO_A_CENTIMETRO = 100

# Se hace las conversiones respectivas
pulgadas = cantidad_pies * PIE_A_PULGADAS
yardas = cantidad_pies / YARDA_A_PIE
centimetros = pulgadas * PULGADA_A_CENTIMETROS
metros = centimetros / METRO_A_CENTIMETRO

# Se imprime los resultados
print(f"Pulgadas: {pulgadas}")
print(f"Yardas: {yardas}")
print(f"Centimetros: {centimetros}")
print(f"Metros: {metros}")
