print("Asignaturas optativas Año 2022")
print("Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")

opcion=input("Escribe la asignatura escogida: ")
asignaturas=opcion.lower()

if asignaturas in("Informatica grafica","Pruebas de software","Usabilidad y accesibilidad"):
	print("Asignatura elegida " + asignaturas)
else:
	print("La asignatura escogida no existe")

# Comparador IN compara si el elemento esta dentro de la variable devuelve TRUE