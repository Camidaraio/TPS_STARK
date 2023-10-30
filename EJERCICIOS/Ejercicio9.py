"""
Ejercicio 9:
Dadas las siguientes listas:
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
y considerando que la posición en la lista corresponde a la misma persona,
mostar el nombre de la persona más joven
"""

lista_edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]



menor_edad = None
nombre_menor_edad = None

for indice in range(len(lista_edades)):
    if menor_edad is None or lista_edades[indice] < menor_edad:
        menor_edad = lista_edades[indice]
        nombre_menor_edad = nombre[indice]

print("La persona más joven es:", nombre_menor_edad)