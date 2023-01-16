""" Ejemplo de bucle while 
i=1

while i<=10:
	print("Ejecucion " + str(i))
	i=i+1

print("termino la ejecucion") """ 
#--------------------------------------------------------------------------
""" Ejemplo de bucle while infinito 
edad=int(input("Introduce tu edad: "))

while edad<0 or edad>100:
	print("Edad incorrecta.")
	edad=int(input("Introduce tu edad: "))
print("Gracias")
print("Su edad es " + str(edad)) """
#--------------------------------------------------------------------------
import math

print("Programa de calculo de raiz cuadrada")
numero=int(input("Introduce un numero: "))

intentos=0

while numero<0:
	print("No se puede hallar la raiz de un numero negativo")

	if intentos==2:
		print("Has superado el numero de intentos")
		break;

	numero=int(input("Introduce un numero: "))
	if numero<0:
		intentos=intentos+1
if intentos<2:
	solucion=math.sqrt(numero)
	print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))
