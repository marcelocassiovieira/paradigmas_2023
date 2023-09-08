"""
Últimos dígitos ¿Cómo usaría el operador resto (%) para obtener el valor del último dígito de un número entero?
¿Y cómo obtendría los dos últimos dígitos? Desarrolle un programa que cargue un número entero por teclado,
y muestre el último dígito del mismo (por un lado) y los dos últimos dígitos (por otro lado).
"""

from src.utils.validar import validar_si_es_numerico
# Se ingresa el numero
numero = int(validar_si_es_numerico("Ingrese el numero:"))

# Se obtiene la ultima unidad y la ultima decena del numero
ultimo_digito = numero % 10
dos_ultimo_digito = numero % 100


# Se imprime los resultados
print(f"Ultimo numero: {ultimo_digito}")
print(f"dos ultimos numeros: {dos_ultimo_digito}")