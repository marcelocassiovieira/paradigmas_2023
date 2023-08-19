# Multiplicación. Ingresar un número cualquiera por teclado y que muestre su respectiva tabla del 1 al 10.

# Ingreso el numero
numero = int(input("Ingrese el numero:"))

# Calculo e imprimo la tabla para el numero dado
for num in range(1, 11):
    result = numero * num
    print(f"{numero} x {num} = {result}")
