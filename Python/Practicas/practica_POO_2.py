class Vehicles():

	def __init__(self,marca,modelo):
		
		self.marca=marca
		self.modelo=modelo
		self.enMarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):

		self.enMarcha=True

	def acelerar(self):

		self.acelera=True

	def frenar(self):

		self.frena=True

	def estado(self):
		print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class Moto(Vehicles): #Herencia de clase
	hcaballito="No hace el caballito"

	def caballito(self):
		self.hcaballito="Voy haciendo el caballito"

	def estado(self):
		print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)

class Furgoneta(Vehicles):

	def carga(self,cargar):
		self.cargado=cargar
		if(self.cargado):
			return "La furgoneta esta cargada"
		else:
			return "La furgoneta esta descargada"

class Electricos():

	def __init__(self):
		self.autonomia=100

	def Charge(self):
		self.cargando=True

class BiciElectrica(Vehicles,Electricos):
	pass

miMoto=Moto("Honda","CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

miBici=BiciElectrica("f","d")