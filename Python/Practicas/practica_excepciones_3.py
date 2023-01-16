def evaluadEdad(edad):
	if edad<0:
		raise TypeError("No se permite edades negativas") #Para forzar nosotros la excepcion sin capturar
	if edad<20:
		return "eres muy joven "
	elif edad<40:
		return "Eres joven "
	elif edad<65:
		return "Jubilacion "
	elif edad<100:
		return "La muerte viene a por ti "
print(evaluadEdad(15))