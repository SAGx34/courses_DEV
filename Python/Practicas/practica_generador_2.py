def devuelveCiudad(*ciudades):
	for elemento in ciudades:
		#for subElemento in elemento:
			yield from  elemento

ciudades=devuelveCiudad("Madrid","Barcelona","Bilbao","Cordoba")
print(next(ciudades))
print(next(ciudades))