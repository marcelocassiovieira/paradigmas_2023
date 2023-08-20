"""
Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio y luego, proponga una dirección de
mail para el nombre y apellido ingresado de acuerdo a las siguientes reglas: Componer la dirección de correo de la
siguiente manera: @ Por ejemplo para Nombre = Felipe, Apellido= Steffolani y Dominio= umet.edu.ar la dirección de
mail sería: fsteffolani@umet.edu.ar. Pero si la primera primera letra del nombre y la primera letra del apellido
son la misma entonces uƟlizar: .@ Por ejemplo para Nombre= Soledad, Apellido= Steffolani y
Dominio= colegiorosarito.edu.ar la direccióºn de mail sería: soledad.steffolani@umet.edu.ar
"""

# Ingreso los datos de entrada
nombre = str(input("Ingrese el nombre: "))
apellido = str(input("Ingrese el apellido: "))
dominio = "@" + str(input("Ingrese el dominio: "))

# Construyo la direccion de email
if nombre[0].lower() == apellido[0].lower():
    email = nombre.lower() + apellido.lower() + dominio
else:
    email = nombre[0].lower() + apellido.lower() + dominio

print(email)
