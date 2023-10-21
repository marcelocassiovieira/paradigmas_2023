"""
Complejo de cines: Desarrollar un programa que permita procesar funciones de un complejo de cines.
Por cada función se conoce:cantidad de espectadores y descuento(S/N).
La carga termina cuando la cantidad de espectadores sea igual a 0(cero).
El programa deberá:
Calcular la recaudación total del complejo,considerando que el valor de la entrada e sde$50en
los días con descuento y $75 en los días sin descuento.
Determinar cuántas funciones con descuentos efectuaron y qué porcentaje representan sobre el total de funciones
"""

flag = True

acum_recaudacion_con_descuento = 0.0
acum_recaudacion_sin_descuento = 0.0
cont_recaudacion_con_descuento = 0

while flag:
    cant_espectadores = int(input("Cantidad de espectadores: "))
    if cant_espectadores == 0:
        flag = False
        break

    con_descuento = input("Tiene descuento? ")

    if con_descuento == "S":
        precio = 50.0
        cont_recaudacion_con_descuento += 1
        acum_recaudacion_con_descuento += precio * cant_espectadores
    else:
        precio = 75.0
        acum_recaudacion_sin_descuento += precio * cant_espectadores


acum_recaudacion =    acum_recaudacion_sin_descuento + acum_recaudacion_con_descuento

print(f"Total recaudacion:{acum_recaudacion}")
print(f"Porcentage de recauacion funciones con descuento:{(acum_recaudacion_con_descuento / acum_recaudacion) * 100}%")
