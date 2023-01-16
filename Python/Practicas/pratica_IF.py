print("Programa de evaluacion de notas de alumnos")

nota_alumno=input("Introduce nota del alumno: ")

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="Suspenso"
	return valoracion

print(evaluacion(int(nota_alumno)))