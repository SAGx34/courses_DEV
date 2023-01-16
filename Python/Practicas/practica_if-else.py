""" CONDICIONAL IF + ELSE

print("Verificacion de acceso")

edad_usuario=int(input("introduce tu edad, por favor: "))

if edad_usuario<18:
	print("Acceso Denegado")
elif edad_usuario>100:
	print("Edad incorrecta")
else:
	print("Acceso Concedido") """


print("Verificacion de notas")

nota_alumno=int(input("Introduce tu nota: "))

if nota_alumno<5:
	print("Insuficiente")

elif nota_alumno<6:
	print("Suficiente")

elif nota_alumno<7:
	print("Bien")

elif nota_alumno<9:
	print("Notable")

else:
	print("Sobresaliente")