class Coche():
	
	def __init__(self): #Constructor que da un estado inicial a todos los objetos de esta clase

		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4 #Se usa el doble guion bajo para encapsular una variable
		self.__enMarcha=False

	def arrancar (self,arrancamos):
		self.__enMarcha=arrancamos

		if(self.__enMarcha):
			chequeo=self.__check()

		if(self.__enMarcha and chequeo):
			return "El coche esta en marcha"

		elif(self.__enMarcha and chequeo==False):
			return("Algo ha ido mal en el chequeo. No se puede arrancar")	

		else:
			return "El coche esta parado"

		self.__enMarcha=True

	def estado(self):
		print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

	def __check(self):
		print("Realizando chequeo")

		self.__gasolina="ok"
		self.__aceite="ok"
		self.__puertas="cerradas"

		if(self.__gasolina=="ok" and self.__aceite=="ok" and self.__puertas=="cerradas"):
			return 	True
		else:
			return False

miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("------------------A continuacion creamos el segundo objeto------------------")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()