"""
Suma - División - Potencia. Se necesita desarrollar un programa que permita calcular la suma de tres números.
Si el resultado es mayor a 10 dividir por 2 (mostrar su resultado sin decimales),
en caso contrario elevar el resultado al cubo.
"""
# Ingreso de los numeros
numero1 = float(input("Ingrese el numero 1:"))
numero2 = float(input("Ingrese el numero 2:"))
numero3 = float(input("Ingrese el numero 2:"))

# Suma de los numeros
resultado = numero1 + numero2 + numero3

# Evalua, calcula e imprime el resultado
if resultado > 10:
    print(int(resultado / 2))
else:
    print(int(resultado**3))



