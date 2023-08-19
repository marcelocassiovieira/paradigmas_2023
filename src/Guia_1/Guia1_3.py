# Escriba un programa que transforme todas las letras de una palabra en mayúsculas, minúsculas y la primera con minúsculas(capitalización).

# Solicito la palabra al usuario
palabra = str(input("Ingrese la palabra:  "))

# Transformo la palabra en mayuscula
mayuscula = palabra.upper()

# Transformo la palabra en minuscula
minuscula = palabra.lower()

# Transformo la palabra con solamente la primera letra en mayuscula
capitalize = minuscula.capitalize()

# Imprimo los resultados
print(mayuscula, minuscula, capitalize)

