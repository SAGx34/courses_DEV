print("Introduce dos numeros")

num1=int(input("Primer numero: "))

num2=int(input("Segundo numero: "))

def Devuelve_max(n1, n2):
	if n1>n2:
		print (n1) 
	elif n2>n1: 
		print (n2)
	else:  
		print("Son iguales")

print("El numero mas alto es: ")

Devuelve_max(num1, num2)