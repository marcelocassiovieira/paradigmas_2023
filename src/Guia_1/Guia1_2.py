# Escribir un programa que pregunte un nombre de usuario, y que después muestre por pantalla si su cantidad de letras es par o impar.

# Solicito el nombre del usuario
nombre = str(input("Ingrese el nombre del usuario:  "))

# Calculo si la cantidad de caracteres en par o impar
par_impar = len(nombre) % 2 == 0

# Asigno el resultado a la variable
resultado = "par" if par_impar else "impar"

# Imprimo el resultado
print(f"La cantidad de letras en el nombre es {resultado}.")


