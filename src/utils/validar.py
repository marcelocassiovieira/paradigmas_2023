def validar_si_es_numerico(texto_entrada):
    is_valid = True
    while is_valid:
        entrada = input(texto_entrada)
        if not entrada.isnumeric():
            try:
                float(entrada)
                is_valid = False
                return entrada
            except ValueError:
                print("")
            print("------------------------------------")
            print("El valor ingresado no es numerico...")
        else:
            is_valid = False
            return entrada


def validar_opciones_correctas(texto, opciones):
    is_valid = False
    while not is_valid:
        opcion = int(validar_si_es_numerico(texto))
        if opcion not in opciones:
            print("------------------------------------")
            print("La opción es invalida...")
        else:
            is_valid = True
            return opcion

