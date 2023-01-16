contador=0
myemail=input("Introduce tu direccion de email: ")

for i in myemail:
	if(i=="@" or i=="."):
		contador=contador+1

if contador>=2:
	print("Email valido")
else:
	print("Email no valido")









	#print("Hola", end=" ") End imprime todo en la misma linea
	#for i range(5): 		range es un tipo que crea una lista o array con el numero de elemtos que se le asigne
