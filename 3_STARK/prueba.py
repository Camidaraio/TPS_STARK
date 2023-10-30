from data_stark import lista_personajes
from tp3_5 import *




# nombre_heroe = obtener_dato(lista_personajes[0], "nombre")

# if nombre_heroe is not False:
#     print(f"Nombre del héroe: {nombre_heroe}")
# else:
#     print("No se encontró la clave o el diccionario está vacío.")

# for heroe in lista_personajes: #Me muestra todos
#     obtener_nombre(heroe)

# if lista_personajes:
#     obtener_nombre(lista_personajes[0])  # Muestra el nombre del primer héroe
# else:
#     print("La lista de personajes está vacía.")


# resultado = obtener_nombre_y_dato(lista_personajes, "fuerza")
# if resultado:
#     print(resultado)  # Esto imprimirá: "Nombre: Venom | fuerza: 500"
# else:
#     print("No se encontró el héroe o la clave especificada.")


# minimo = obtener_minimo(lista_personajes, "fuerza")
# print(minimo)


# # Ejemplo de uso
# mayor_altura = obtener_maximo(lista_personajes, "altura")
# lista_heroes_max_altura = obtener_dato_cantidad(lista_personajes, mayor_altura, "altura")

# for heroe in lista_heroes_max_altura:
#     print(f"Nombre: {heroe['nombre']}, Altura: {heroe['altura']}")

# mas_pesado = obtener_maximo(lista_personajes, "peso")
# lista_mas_pesados = obtener_dato_cantidad(lista_personajes,mas_pesado , "peso")
# stark_imprimir_heroes(lista_mas_pesados)

#stark_imprimir_heroes(lista_personajes)

# resultado = dividir(lista_personajes, "fuerza")

# if resultado is not False:
#     print(f"La suma de las edades de los héroes es: {resultado:.2f}")
# else:
#     print("No se pudo calcular la suma.")


# resultado = calcular_promedio(lista_personajes, "fuerza")
# if resultado is not False:
#     print(f"El promedio de la clave héroes es: {resultado:.2f}")
# else:
#     print("No se pudo calcular el promedio.")

# numero = "12345"
# es_valido = validar_entero(numero)

# if es_valido:
#     print("Es string.")
# else:
#     print("No es string.")


# # Ejemplo de uso
# opcion_elegida = stark_menu_principal()

# if opcion_elegida is not False:
#     print(f"Ha elegido la opción {opcion_elegida}")

# stark_marvel_app(lista_personajes)

# # Ejemplo de uso
# mayor_altura = obtener_maximo(lista_personajes, "altura")
# lista_heroes_max_altura = obtener_dato_cantidad(lista_personajes, mayor_altura, "altura")

# for heroe in lista_heroes_max_altura:
#     print(f"Nombre: {heroe['nombre']}, Altura: {heroe['altura']}")

# stark_marvel_app()


#---------------------------MENU---------

while True:
    print (
    "\nBienvenido a Stark Marvel App \n"
    "1.  Normalizacion de datos\n",
    "2. Mostrar el nombre de un héroe\n",
    "3. Obtener un nombre y un dato de un héroe\n",
    "4. Mostrar el maximo de una clave\n",
    "5. Mostrar el minimo de una clave\n",
    "6. representacion de un valor de una clave de varios heroes\n",
    "7. Mostrar clave, valor de cada heroe\n",
    "8. suma de valores de una lista\n",
    "9. dividi de valores de una lista\n",
    "10. promedio de valores de una lista\n"
    "11. Salir  \n",
    ) 

    opcion = input("Elija una opcion del 1 a 11: ")
    opcion_int = int(opcion)
    match(opcion_int):
        case 1:
            resultado = normalizar_datos(lista_personajes)
        case 2:
            nombre_heroe = obtener_dato(lista_personajes[0], "nombre")
            print(nombre_heroe)
            print("\n")
        case 3:
            resultado = obtener_nombre_y_dato(lista_personajes, "fuerza")
            if resultado:
                print(resultado)  # Esto imprimirá: "Nombre: Venom | fuerza: 500"
            else:
                print("No se encontró el héroe o la clave especificada.")
        case 4:
            maximo = obtener_maximo(lista_personajes, "fuerza")
            print("El maximo es: ", maximo)
        case 5:
            minimo = obtener_minimo(lista_personajes, "fuerza")
            print("El minimo es: ",minimo)
        case 6:
            mas_pesado = obtener_maximo(lista_personajes, "peso")
            lista_mas_pesados = obtener_dato_cantidad(lista_personajes,mas_pesado , "peso")
            stark_imprimir_heroes(lista_mas_pesados)
        case 7:
            mas_pesado = obtener_maximo(lista_personajes, "peso")
            lista_mas_pesados = obtener_dato_cantidad(lista_personajes,mas_pesado , "peso")
            stark_imprimir_heroes(lista_mas_pesados)
        case 8:
            resultado_suma = sumar_dato_heroe(lista_personajes, "fuerza")
            print(resultado_suma)
        case 9:
            resultado_dividir = dividir(100, 10000)
            print(resultado_dividir)
        case 10:
            resultado = calcular_promedio(lista_personajes, "fuerza")
            if resultado is not False:
                print(f"El promedio de la clave héroes es: {resultado:.2f}")
            else:
                print("No se pudo calcular el promedio.")
        
        case _:
            break



