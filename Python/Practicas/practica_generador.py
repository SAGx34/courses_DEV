""" def numerosPares(limite):

	num=1

	while num<limite:

		yield num*2

		num=num+1
pares=numerosPares(20)

for i in pares:

	print(i)


	"""
	

def numerosPares(limite):

	num=1

	while num<limite:

		yield num*2

		num=num+1
pares=numerosPares(20)

print(next(pares))

print("Aqui podria haber mas cogido")

print(next(pares))

print("Aqui podria haber mas cogido")

print(next(pares))