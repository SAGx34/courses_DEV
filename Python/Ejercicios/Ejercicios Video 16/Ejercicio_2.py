passw=input("Introduce una contraseña con un minimo de 8 caracteres y sin espacios en blanco: ")

contador=0

for i in range(len(passw)):
	if passw[i]==" ":

		contador=1

if len(passw)<8 or contador>0:
	print("Contraseña no valida")

else:
	print("Contraseña valida")



