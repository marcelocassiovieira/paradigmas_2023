""""
Cuadrado de un binomio. Plantear un script directamente en el shell de Python, que permita mostrar,
para dos valores 𝑎 y 𝑏, que: Un binomio al cuadrado (suma) es igual al cuadrado del primer término,
más el doble producto del primero por el segundo más el cuadrado del segundo.
"""

from src.utils.validar import validar_si_es_numerico

# Solicito el ingreso de los numeros
a = float(validar_si_es_numerico("Ingrese el primer numero: "))
b = float(validar_si_es_numerico("Ingrese el segundo numero: "))

# Se reemplaza los valores en la funcion y se evalua
esperado = a**2 + 2*a*b + b**2 == (a + b)**2

# Se asigna el valor booleano correspondiente a la variable
resultado = "Se cumple" if esperado else "No se cumple"

# Se imprime el resultado guardado en variable
print(resultado)



