"""
Elecciones presidenciales.
Según la Ley Electoral de la República ArgenƟna, el Presidente y el Vicepresidente se eligen de acuerdo a las
siguientes reglas:
Artículo 149. — Resultará electa la fórmula que obtenga más del cuarenta y cinco por ciento (45 %) de los votos
afirmativos válidamente emitidos; en su defecto, aquella que hubiere obtenido el cuarenta por ciento (40 %)
por lo menos de los votos afirmativos válidamente emitidos y, además, existiere una diferencia mayor de diez
puntos porcentuales respecto del total de los votos afirmativos válidamente emitidos sobre la fórmula que le sigue en
número de votos.
Artículo 150. — Si ninguna fórmula alcanzare esas mayorías y diferencias de acuerdo al escrutnio ejecutado por las
Juntas Electorales, y cuyo resultado único para toda la Nación será anunciado por la Asamblea Legislativa atento lo
dispuesto por el arơculo 120 de la presente ley, se realizará una segunda vuelta dentro de los treinta (30) días.
Articulo 151. — En la segunda vuelta parƟciparán solamente las dos fórmulas más votadas en la primera, resultando electa
la que obtenga mayor número de votos afirmativos válidamente emiƟdos.

Desarrollar un programa que permita ingresar, para los 3 parados más votados: fórmula (presidente + vice) y cantidad de
votos obtenidos. Luego determinar: Qué fórmula obtuvo el mayor porcentaje. Si la fórmula resulta elegida o se requiere
segunda vuelta. En este caso, indicar también quienes parƟcipan de la segunda vuelta.
"""

# Definiciones
votos_porcentage = {}
formula = {}
elecciones = {}
formulas = {
    1: "Milei | Villarruel",
    2: "Patricia Bullrich | Luis Petri",
    3: "Sergio Massa | Agustín Rossi"
}

partidos = {
    1: "La libertad avanza",
    2: "Juntos por el cambio",
    3: "Union por la patria",
}

iteracciones = len(partidos)

for num in range(iteracciones):
    for numero, nombre in partidos.items():
        print(numero, ":", nombre)

    opcion = int(input("Indique el numero de opcion del partido: "))
    print("*************")
    print("Completar los nombre de presidente y vice")
    print("1 - Carga manual")
    print("2 - Seleccionar desde la lista")

    escribir_o_completar = int(input("indique la opcion: "))
    if escribir_o_completar == 1:
        presidente = str(input("Indique el nombre del presidente de la formula: "))
        vice = str(input("Indique el nombre del vicepresidente de la formula: "))

    elif escribir_o_completar == 2:
        print("*************")
        for clave, valor in formulas.items():
            print(clave, "-", valor)

        opcion_formula = int(input("Selecciona la opcion de la formula:"))
        presidente = formulas[opcion_formula].split("|")[0].strip()
        vice = formulas[opcion_formula].split("|")[1].strip()

    print("*************")
    cant_votos = int(input("Indique la cantidad de votos para la formula elegida:"))
    print("*************")
    elecciones[opcion] = cant_votos


total_votos = 0
for sum in elecciones:
    total_votos += elecciones[sum]

for sum in elecciones:
    votos_porcentage[sum] = elecciones[sum] / total_votos * 100

mayor_clave = None
mayor_valor = float("-inf")
for clave, valor in votos_porcentage.items():
    if valor > mayor_valor:
        mayor_valor = valor
        mayor_clave = clave

del votos_porcentage[mayor_clave]

segundo_mayor_clave = None
segundo_mayor_valor = float("-inf")
for clave, valor in votos_porcentage.items():
    if valor > segundo_mayor_valor:
        segundo_mayor_valor = valor
        segundo_mayor_clave = clave


es_ganador = mayor_valor >= 45 or (mayor_valor >= 40 and mayor_valor - segundo_mayor_valor > 10)

print("Formula con mas votos: ", formulas[mayor_clave], "{:.2f}".format(mayor_valor), "%")
if es_ganador:
    print("Es ganador en primera vuelta!!!: ")
    print("Segundo lugar: ", formulas[segundo_mayor_clave], "{:.2f}".format(segundo_mayor_valor), "%")
else:
    print("Van a segunda vuelta las formulas: ", formulas[mayor_clave], "vs",   formulas[segundo_mayor_clave])
    print(formulas[mayor_clave], "{:.2f}".format(mayor_valor), "%")
    print(formulas[segundo_mayor_clave], "{:.2f}".format(segundo_mayor_valor), "%")


