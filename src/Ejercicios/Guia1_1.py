# Desarrolle un programa que pase un peso de kilogramo a libras teniendo en cuenta que cada kilogramo equivale a 2.2 libras.

# Defino la constante de la equivalencia kg - lb
KILO_TO_LIBRA_VALUE = 2.2


# Solicito al usuario que ingrese la cantidad de kilo a convertir
cantidad_kilos = int(input("Ingrese la cantidad de kilos a convertir:  "))

# Hago la conversion de kilos a libras
cantidad_libras =  cantidad_kilos * KILO_TO_LIBRA_VALUE;


#Imprimo la cantidad de libras
print(cantidad_kilos , f" kilos equivalen a {cantidad_libras} libras.")


