""""
Cuadrado de un binomio. Plantear un script directamente en el shell de Python, que permita mostrar,
para dos valores 𝑎 y 𝑏, que: Un binomio al cuadrado (suma) es igual al cuadrado del primer término,
más el doble producto del primero por el segundo más el cuadrado del segundo.

"""

a = float(input("Ingrese el primer numero"))
b = float(input("Ingrese el segundo numero"))

binomio_al_cuadrado = a**2 + 2*a*b + b**2
esperado = (a + b)**2

resultado = "Se cumple" if binomio_al_cuadrado == esperado else "No se cumple"

print(resultado)


