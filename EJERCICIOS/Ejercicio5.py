"""
Ejercicio 5:
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
por cada estadía como base, se pide el ingreso de una estación del
año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
Plata/Córdoba) para vacacionar para poder calcular el precio final:
-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
descuento del 10% Mar del Plata tiene un descuento del 20%
-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
un aumento del 10% Mar del Plata tiene un aumento del 20%
-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
precio sin descuento.
Validar el ingreso de datos
"""

precio_base = 15000

# Solicitamos el ingreso de la estación del año y la localidad
estacion = input("Ingrese la estación del año (Invierno/Verano/Otoño/Primavera): ").lower()
localidad = input("Ingrese la localidad (Bariloche/Cataratas/Mar del Plata/Córdoba): ").lower()

# Validamos el ingreso de datos
while estacion not in ["Invierno", "Verano", "Otoño", "Primavera"] or localidad not in ["bariloche", "cataratas", "mar del plata", "córdoba"]:
    print("Los datos ingresados no son válidos.")
    estacion = input("Ingrese la estación del año (Invierno/Verano/Otoño/Primavera): ").lower()
    localidad = input("Ingrese la localidad (Bariloche/Cataratas/Mar del Plata/Córdoba): ").lower()

# Calculamos el precio final según la estación y localidad
match (estacion):
    case "Invierno":
        if localidad == "Bariloche":
            precio_final = precio_base * 1.2
        elif localidad in ["Cataratas", "Córdoba"]:
            precio_final = precio_base * 0.9
        else:  # Mar del Plata
            precio_final = precio_base * 0.8

    case "verano":
        if localidad == "Bariloche":
            precio_final = precio_base * 0.8
        elif localidad in ["cataratas", "Córdoba"]:
            precio_final = precio_base * 1.1
        else:  # Mar del Plata
            precio_final = precio_base * 1.2

    case _:  # Otoño y Primavera
        if localidad == "Bariloche":
            precio_final = precio_base * 1.1
        elif localidad == "Cataratas":
            precio_final = precio_base * 1.1
        elif localidad == "Mar del Plata":
            precio_final = precio_base * 1.1
        else:  # Córdoba
            precio_final = precio_base

# Mostramos el precio final al usuario
print(f"El precio final de la estadía es: ${precio_final:.2f}") 