def divide():

	try:

		op1=(float(input("Introduce el primer numero: ")))

		op2=(float(input("Introduce el segundo numero: ")))

		print("La divicion es: " + str(op1/op2))

	except ValueError:

		print("El valor es erroneo")


	except ZeroDivisionError:

		print("No se puede dividir por 0") 
		
	finally:

		print("Calculo finalizado")

divide()