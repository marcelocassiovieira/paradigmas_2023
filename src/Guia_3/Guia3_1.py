"""
Comisión de vendedores.
Una empresa debe calcular el total de comisiones que debe abonar por ventas realizadas
por sus vendedores, para ello les solicita un sistemita que le permita calcular dichos montos.
Se tiene conocimiento que la empresa tiene cuatro categorías de vendedores(1 a 4).
Usted debe solicitar el ingreso de la categoría del vendedor y el total de la venta(el proceso termina cuando se
ingrese una categoría igual a cero) y acumular las comisiones de las ventas rendidas por los vendedores de
diferentes en base a los siguientes cálculos:
Categoría1:cobra una comisión de 10%
Categoría2: cobra una comisión de 25%
Categoría3:cobra una comisión de 30%
Categoría4:cobra una comisión de 40%
Una vez procesadas todas las ventas mostrar el total de comisiones a pagar por cada categoría de vendedor es que
en el la empresa junto con el total general.
"""
from src.utils.validar import validar_opciones_correctas

# crear un diccionario con las categorias
categorias = {
    0: 0,
    1: 10,
    2: 20,
    3: 30,
    4: 40
}

total_comisiones = 0
total_ventas = 0

carga_datos = True

while carga_datos:
    # validar categorias de vendedor
    cat_vendedor = validar_opciones_correctas("Ingresa la categoria del vendedor: ", list(categorias.keys()))

    if cat_vendedor == 0:
        carga_datos = False
        print("Saliendo...")
        break

    # pedir el monto de la venta
    monto_venta = float(input("Ingresa el monto de la venta: "))
    total_comisiones += monto_venta * categorias[cat_vendedor]/100
    total_ventas += monto_venta


print(f"Total de comisiones: {total_comisiones}")
print(f"Total de ventas: {total_ventas}")
print(f"Total general: {total_ventas + total_comisiones}")







