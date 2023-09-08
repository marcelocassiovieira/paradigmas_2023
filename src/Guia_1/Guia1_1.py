# Desarrolle un programa que pase un peso de kilogramo a libras teniendo en cuenta que cada kilogramo equivale a 2.2 libras.

from src.utils.validar import validar_si_es_numerico

# Defino la constante de la equivalencia kg - lb

KILO_TO_LIBRA_VALUE = 2.2

# Solicito al usuario que ingrese la cantidad de kilo a convertir uso una funcion para validar si es numerico
cantidad_kilos = float(validar_si_es_numerico("Ingrese la cantidad de kilos a convertir:  "))

# Hago la conversion de kilos a libras
cantidad_libras =  cantidad_kilos * KILO_TO_LIBRA_VALUE;

#Imprimo la cantidad de libras
print(cantidad_kilos , f" kilos equivalen a {cantidad_libras} libras.")


