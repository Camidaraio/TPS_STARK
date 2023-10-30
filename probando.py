# mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Ejemploville"}

# for clave, valor in mi_diccionario.items():
#     print(f"Clave: {clave}, Valor: {valor} ")

import re
texto = ' uno 1 dos 2 tres 3 cuatro'
# print(re.search(' ', texto))
# #<re.Match object; span=(0, 1), match=' '>
# print(re.search('[0-9]+', texto))
# #<re.Match object; span=(5, 6), match='1'>
# print(re.search('[a-z ]+', texto))
# #<re.Match object; span=(0, 5), match=' uno '>

#----------- FINDALL -------------------

#Devuelve con \D todo aquello que no son numeros del texto indicado. (Devuelve strig)
resultado = re.findall(r"\D", texto)
print(resultado)

#Devuelve con \d todo aquello que son numeros.
resultado = re.findall(r"\d", texto)
print(resultado)
 
#Devuelve con \w caracteres alfanumericos [a-z A-Z 0-9 _].
resultado = re.findall(r"\w", texto)
print(resultado)

#Devuelve con \W todo menos caracteres alfanumericos [a-z A-Z 0-9 _]. s decir punto, comas, llaves, etc.
resultado = re.findall(r"\W", texto)
print(resultado)
#------------------  ----------------

