votos: {}

formulas = {
    1: "La libertad avanza - Milei | Villarruel",
    2: "Juntos por el cambio - Patricia Bullrich | Luis Petri",
    3: "Union por la patria - Sergio Massa | Agustín Rossi"
}

print("Seleccione la opcion: ")
for clave in formulas:
    valor = formulas[clave]
    print(f"Formula: {clave}, Valor: {valor}")


opcion = int(input(": "))
cant_votos = int(input("Ingrese la cantidad de votos: "))

votos[opcion] = cant_votos

print(votos)
