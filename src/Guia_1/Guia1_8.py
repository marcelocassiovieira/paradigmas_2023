# Ingresar la cantidad de números de la sucesión de Fibonacci a mostrar.

from src.utils.validar import validar_si_es_numerico
# Ingresa la cantidad
cantidad = int(validar_si_es_numerico("Ingrese la cantidad para la sucesion de fibonacci: "))

# Se inicializa variables
a = 0
b = 1
result = 0;


# Se imprime los primeros dos numeros de la sucecion porque no llevan los primeros calculos
print(a)
print(b)

# Se itera y se calcula los otros numeros de la secuencia, imprimiendolos
while result <= cantidad:
    result = a + b
    print(result)
    a = b
    b = result





