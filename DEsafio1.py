#elaborar un programa en Python que permita emitir un mensaje de acuerdo a lo que una persona ingresa como cantidad de años
#que viene usando insecticida en su plantación. Si hace 10 o más añoss, 
#debemos emitir el mensaje "Por favor solicite revisión de suelos en su plantación".
#Si hace menos de 10 años, debemos emitir el mensaje "Intentaremos ayudarte con un nuevo sistema de control de plagas, 
#y cuidaremos el suelo de tu plantación". #

print("Bienvenido al sistema de gestion del control de plagas")

años = None

años = int(input("Ingrese la cantidad de años que viene usando insecticidad para el control de plagas "))

if años >= 10:
	print("-> Por favor solicite revisión de suelos en su plantación")

else:
	print("-> Intentaremos ayudarte con un nuevo sistema de control de plagas y cuidaremos el suelo de tu plantación")