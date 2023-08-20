# Crear un conversor de pies y pulgadas a centímetros.

# Se solicita el tipo de conversion
print("Seleccione una opción:")
print("1. Convertir pies a centimetros")
print("2. Convertir pulgadas a centimetros")
opcion = int(input("Seleccione el numero de la opcion: "))

# Se solicita la cantidad
cantidad = int(input("Ingresa la cantidad: "))

# Declaro las constantes de equivalencia
PIE_A_CENTIMETRO = 30.48
PULGADA_A_CENTIMETRO = 2.54

# Formato del texto
texto_singular_o_plural = ("s" if cantidad > 1 else "")

# Se calcula en base a la opcion y se imprime
if opcion == 1:
    resultado = cantidad * PIE_A_CENTIMETRO
    print(f"{cantidad} pie{texto_singular_o_plural} corresponden a {resultado} centimetros")

if opcion == 2:
    resultado = cantidad * PULGADA_A_CENTIMETRO
    print(f"{cantidad} pulgada{texto_singular_o_plural} corresponden a {resultado} centimetros")

