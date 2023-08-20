"""
Galería de Arte. Una galería de arte desea preparar un catálogo de sus cuadros más famosos.
Se realiza una prueba con tres cuadros y por cada uno se ingresa el año en que fue creado.
El programa deberá verificar si todos los cuadros son anteriores al siglo XX (El siglo XX es el siglo pasado.
Se inició en el año 1901 y terminó en el año 2000). Determinar cuántos tienen antigüedad inferior a 10 años.
Si no hay ninguno, imprimir el mensaje “Renovar stock”.
"""

# Definifo variables
cantidad_de_cuadros = 3
cant_cuadros_menor_10_anios = 0
anio_corriente = 2023

# Evaluo la antiguedad de los cuadros
for cant in range(cantidad_de_cuadros):
    anio_creacion = int(input("Ingrese el año:"))
    if anio_creacion < 1901:
        print("EL cuadro es anterior al siglo XX")
    else:
        print("EL cuadro no es anterior siglo XX")
        if anio_corriente - anio_creacion < 10:
            cant_cuadros_menor_10_anios += 1

# Impresion de los resultados con logica segun consigna
print("************************************************************")
print(f"{cant_cuadros_menor_10_anios} Cuadros con intiguedad inferior a 10 años" if cant_cuadros_menor_10_anios > 0 else "Renovar stock")