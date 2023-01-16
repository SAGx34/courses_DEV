""" Continue se usa para saltar un recorrido del bucle

nombre="pildoras informaticas"

contador=0

for i in nombre:
	if i==" ":
		continue
	contador+=1
	
print(contador) """

""" Class se utiliza para devolver un valor nulo
class MiClase:
	pass """

email=input("Por favor introduce tu email: ")

for i in email:
	if i=="@":
		arroba=True
		break;
else: #se ejecuta cuando el bucle queda vacio
	arroba=False
print(arroba)