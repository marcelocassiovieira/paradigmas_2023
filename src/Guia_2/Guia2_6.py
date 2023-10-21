"""
Mostrar por pantalla el promedio de los números ingresados por teclado. Se deja de pedir que el usuario agregue
números una vez ingrese 0 (cero).
"""

flag = True
acum_total = 0
contador = 0
while flag:
    numero = int(input("Ingrese el primer numero: "))
    if numero == 0:
        flag = False
    else:
        acum_total = acum_total + numero
        contador = contador + 1

print(f"Valor promedio: {acum_total / contador}")
