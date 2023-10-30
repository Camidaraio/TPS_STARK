"""
Ejercicios:

Ejercicio 1:
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
sueldo para esa persona.



"""

nombre = input("Ingrese su nombre")
sueldo = input("Ingrese su sueldo") 
sueldo_int = int(sueldo)
incremento = sueldo_int * 0.10 
sueldo_int += incremento 
print(sueldo_int)


