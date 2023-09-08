"""
Sueldos y aguinaldo. Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego:
a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.
b) Determinar en qué mes recibió el sueldo más bajo del período.
c) Informar el sueldo promedio del semestre.
"""
from src.utils.validar import validar_opciones_correctas

INDEX_SUELDO = 1
INDEX_MES = 0

mes_sueldo = {}
meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "junio"
}

print("Vamos a completar los suelos de los primeros 6 meses del año: ")
for num, mes in meses.items():
    print(f"{num}: {mes}")
    sueldo = float(input("Ingrese el sueldo: "))
    mes_sueldo[num] = sueldo

# sueldo_mas_alto = next(iter(mes_sueldo.items()))

sueldo_mas_alto = next(iter(mes_sueldo.items()))
sueldo_mas_bajo = next(iter(mes_sueldo.items()))

for mes, sueldo in mes_sueldo.items():
    if sueldo > sueldo_mas_alto[1]:
        sueldo_mas_alto = mes, sueldo

for mes, sueldo in mes_sueldo.items():
    if sueldo < sueldo_mas_bajo[1]:
        sueldo_mas_bajo = mes, sueldo

total_sueldos =  sum(mes_sueldo.values())

print("*****************************************")
print(f"Aguinaldo: ${sueldo_mas_alto[INDEX_SUELDO] / 2}")
print(f"Sueldo mas bajo del periodo: {meses[sueldo_mas_bajo[INDEX_MES]]} ${sueldo_mas_bajo[INDEX_SUELDO]}")
print(f"Sueldo promedio del periodo: ${total_sueldos / len(meses)}")