"""
Jornal de un Operario. Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita
informar el jornal de un determinado operario. Usted deberá cargar por teclado el código de turno que el operario
trabajó ese día (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas. La política de
trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno diurno o nocturno. Si un operario
trabaja en el turno nocturno el pago es 40.60 pesos la hora, si lo hace en el turno diurno cobra 35.50 pesos la hora.
"""
from src.utils.validar import validar_opciones_correctas
from src.utils.validar import validar_si_es_numerico

# Definicion de las variables y constantes
TARIFA_NOTURNA = 40.60
TARIFA_DIURNA = 35.50
codigo_turno = 0
opciones = [1, 2]

# Se cargan los datos por pantalla y validacion de la opcion
while codigo_turno != 1 and codigo_turno != 2:
    print("1- Representa Diurno")
    print("2- Representa Nocturno")
    codigo_turno = int(validar_opciones_correctas("Ingrese el número de la opción deseada: ", opciones))
    print("************* Opcion invalida! *************" if codigo_turno != 1 and codigo_turno != 2 else "")

# Carga de las horas
cant_horas = int(validar_si_es_numerico("Indique la cantidad de horas trabajadas: "))

# Calculo segun tarifa
if (codigo_turno == 1):
    jornal = cant_horas * TARIFA_DIURNA
elif (codigo_turno == 2):
    jornal = cant_horas * TARIFA_NOTURNA

# Impresion del resultado
print(f"El jornal del operario es de: ${jornal} pesos.")

