print("Programa de becas año 2022")

distancia_escuela=int(input("Distancia del centro en km "))
print(distancia_escuela)

numero_hermanos=int(input("Numero de hermanos "))
print(numero_hermanos)

salario_familiar=int(input("Salario familiar anual bruto "))
print(salario_familiar)

if distancia_escuela>=40 and numero_hermanos>2 or salario_familiar<=20000:
	print("Cumple los requisitos de beca")
else:
	print("No cumple los requisitos para la beca")

	# AND = Y si. OR = O si no.