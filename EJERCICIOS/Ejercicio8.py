# lista_numeros = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]

# numeros_vistos = set()
# numero_repetido = None

# for numero in lista_numeros:
#     if numero in numeros_vistos:
#         numero_repetido = numero
#         break
#     else:
#         numeros_vistos.add(numero)

# if numero_repetido is not None:
#     print(f"El número repetido es: {numero_repetido}")
# else:
#     print("No se encontraron números repetidos.")
 

#Sin indice
lista_numeros = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
bandera = False
for numero in lista_numeros:
    contador = 0
    for dato in lista_numeros:
        if numero == dato:
            contador += 1
            if contador == 2:
                numero_repetido = numero
                bandera = True
                break
    if bandera == True:
        break
print(numero_repetido)

#CON INDICE

lista_numeros = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
numero_repetido = None

for i in range(len(lista_numeros)):
    for j in range(i + 1, len(lista_numeros)):
        if lista_numeros[i] == lista_numeros[j]:
            numero_repetido = lista_numeros[i]
            break

if numero_repetido is not None:
    print(f"El número repetido es: {numero_repetido}")
else:
    print("No se encontraron números repetidos.")
