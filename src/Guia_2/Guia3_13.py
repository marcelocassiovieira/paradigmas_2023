"""
Desarrollar un programa que permita procesar los datos del último censo de una pequeña población.
Por cada habitante se ingresa:sexo(M/F)y edad.
La carga de datos analiza al ingresar cualquier otro valor para sexo.
El programa debe informar:
A qué sexo corresponde la mayor cantidad de habitantes(considerar que puede ser igual)
Cantidad de mujeres en edad escolar(4 a 18 años inclusive)
Si hay algún varón que supere los 80 años de edad.
"""

flag = True

cont_masc = 0
cont_fem = 0
flag_impresion = True

while flag:
    isValid_sexo = False
    isValid_edad = False

    while not isValid_sexo:
        sexo = input("Ingrese el sexo: ").upper()

        if sexo != "M" and sexo != "F" and sexo != "0":
            print("Ingreso invalido: debe ser F o M o 0")
        else:
            isValid_sexo = True

    if sexo == "0":
        flag_impresion = False
        break

    while not isValid_edad:
        edad = input("Ingrese la edad: ")
        if not edad.isdigit():
            print("Ingreso invalido: debe ser numerico...")
        else:
            isValid_edad = True

    if edad == "0":
        flag_impresion = False
        break

    if sexo == "M":
        cont_masc += 1
    else:
        cont_fem += 1


if flag_impresion:
    print(cont_fem)
    print(cont_masc)
else:
    print("Saliendo del programa...")