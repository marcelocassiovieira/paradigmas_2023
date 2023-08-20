# Escribir un programa que pida dos números y muestre como resultado su división, cociente y resto.

# Se solicita los numeros
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Calcular la división, cociente y resto
division = numero1 / numero2
cociente = numero1 // numero2
resto = numero1 % numero2

# Mostrar los resultados
print("Resultado de la división:", division)
print("Cociente:", cociente)
print("Resto:", resto)