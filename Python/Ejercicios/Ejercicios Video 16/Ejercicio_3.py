contador_arroba=0
contador_punto=0

myemail=input("Introduce tu direccion de email: ")

for i in myemail:
	if(i=="@"):
		contador_arroba=contador_arroba+1
	if(i=="."):
		contador_punto=contador_punto+1


if contador_arroba!=1 or contador_punto==0:
	print("Email no valido")
else:
	print("Email valido")
