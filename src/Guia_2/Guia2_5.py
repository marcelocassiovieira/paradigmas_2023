"""
Analisis de Texto.
El usuario ingresa una frase al comenzar el programa, la misma no puede tener longitud cero.
La frase finaliza con un punto, y las palabras están separadas por espacios únicamente.
Se debe mostrar:
a) Ver el porcentaje de vocales respecto del total de letras de la frase.
b) La longitud promedio de las palabras.
c) La longitud de la palabra mas larga del texto.
d) Cantidad de palabras que comienzan con "ta".
"""

is_valid = False
vocales = ["a", "e", "i", "o", "u"]
contador_vocales = 0
cant_caracteres_total = 0
cant_palabras_con_ta = 0

while not is_valid:
    frase = input("Ingrese la frase: ")
    longitud_total = len(frase) - 1
    if longitud_total == 0:
        print("------------------------------------")
        print("No debe estar vacio...")
    else:
        ultimo_digito = frase[longitud_total]
        if not ultimo_digito == ".":
            print("------------------------------------")
            print("El ultimo digito debe ser un punto(.)")
        else:
            frase = frase.replace(".", "").lower()
            palabras = frase.split()

            for letra in frase:
                if letra in vocales:
                    contador_vocales = contador_vocales + 1
            palabra_mas_larga = palabras[0]
            for palabra in palabras:
                cant_caracteres_total = cant_caracteres_total + len(palabra)
                if palabra.startswith("ta"):
                    cant_palabras_con_ta = cant_palabras_con_ta + 1
                if len(palabra) > len(palabra_mas_larga):
                    palabra_mas_larga = palabra

            is_valid = True

            print(f"Porcentage de vocales: + {(contador_vocales / cant_caracteres_total) * 100}%")
            print(f"Longitud promedio de las palabras: {(cant_caracteres_total) / len(palabras)}")
            print(f"Longitud de la palabra mas larga: {len(palabra_mas_larga)}")
            print(f"Cantidad de palabras que empiezan con ta: {cant_palabras_con_ta}")





