""" for i in range(5):
		print(f"valor de la variable {i}") #f concatena un string con el valor de la variable. """

valido=False

email=input("Introduce tu email: ")

for i in range(len(email)):
	if email[i]=="@":

		valido=True

if valido==True:
	print("Email Correcto")
else:
	print("Email Incorrecto")