numero1=int(input("Introduce un numero por favor: "))
numero2=int(input("Introduce un numero mayor que " + str(numero1) + " : "))

while numero2>numero1:
	numero1=numero2
	numero2=int(input("Vuelva a introducir un numero mayor que " + str(numero1) + " : "))

print(str(numero2) + " no es mayor que " + str(numero1))
