# EJEMPLOS DE USO DICCIONARIO

middicionario={"Alemania":"Berlin","Francia":"Paris","Inglaterra":"Londres","España":"Madrid"}
middicionario["Italia"]="Lisboa"
print(middicionario)
middicionario["Italia"]="Roma"
print(middicionario)
del middicionario["Inglaterra"]
print(middicionario)
middicionario["Paises"]=4
print(middicionario) 

# EJEMPLO DE AÑADIR VALORES A LAS CLAVES DEL DICCIONARIO CON TUPLAS 

mitupla=["España","Francia","Inglaterra","Alemania"]
midiccionario={mitupla[0]:"Madrid",mitupla[1]:"Paris",mitupla[2]:"Londres",mitupla[3]:"Berlin"}
print(midiccionario["Francia"]) 

# EJEMPLO DE AÑADIR VARIOS VALORES A UNA CLAVE CON UNA TUPLA Y AÑADIR UN DICCIONARIO DENTRO DE UNO YA CREADO

midiccionario={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario.keys())
print(midiccionario.values())
print(len(midiccionario))
print(midiccionario["Anillos"])