num_positivo=int(input("Introduce un numero positivo: "))
suma=0

while num_positivo>0:
	suma=suma+num_positivo
	num_positivo=int(input("Introduce otro numero positivo: "))

print("La suma de los numeros introducidos es " + str(suma))
