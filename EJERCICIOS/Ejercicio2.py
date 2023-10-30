"""
Ejercicio 2:
Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
adolescente (entre 13 y 17 años) o niño (menor a 13 años).
"""

edad = input("Ingrese su edad: ")
edad_int = int(edad)
if edad_int > 18:
    print("Es mayor")
elif edad_int > 13 and edad_int < 17:
    print("Es adolesente")
else:
    print("Es menor")

