from data_stark import lista_personajes
from punto7 import *

#Camila Daraio

def verificar_no_vacio(lista):
    """
    Verifica si una lista está vacia

    Parametros:
    - lista: La lista que se va a verificar

    Retorna:
    - bool: True si la lista está vacía, False en caso contrario
    """

    if not lista:
        print("Lista vacia")
        return False
    else:
        return True
    

def normalizar_datos(lista):
    """
    Normaliza los datos numericos en la lista de heroes.

    Parametros:
    - lista_personajes: Una lista de diccionarios que representan héroes, donde algunas claves contienen datos numericos.

    Retorna:
    - bool: True si se realizaron cambios en los datos, False en caso contrario

    """
    verificar_no_vacio(lista)

    cambios_realizados = False

    for heroe in lista:
        for clave, valor in heroe.items():
            if type(valor) == str and valor.replace(".", "").isdigit():
                cambios_realizados = True
                if "." in valor:
                    heroe[clave] = float(valor)
                else:
                    heroe[clave] = int(valor)

    if cambios_realizados == True:
        print("Se realizaron cambios en los datos \n")

    return cambios_realizados


def obtener_dato(lista_heroes, clave):
    """
    Obtiene el valor de una clave de un heroe

    Parametros:
    - diccionario: lista_heroes
    - clave: la clave del héroe

    Devuelve:
    - El valor de la clave
    """ 

    if verificar_no_vacio([lista_heroes]) and clave in lista_heroes:
        print(f"Existe la clave '{clave}'")
        return lista_heroes[clave]
    else:
        print(f"No existe la clave en el diccionario")
        return False
    
    # nombre_heroe = obtener_dato(lista_personajes[0], "nombre")

    # # Comprobar si se obtuvo el nombre y mostrarlo
    # if nombre_heroe is not False:
    #     print(f"Nombre del héroe: {nombre_heroe}")
    # else:
    #     print("No se encontró la clave o el diccionario está vacío.")


def obtener_nombre(lista_heroes):
    """
    Obtiene el nombre de un heroe.

    Parametros:
    - heroe: heroe.

    Devuelve:
    - El nombre del heroe.
    """

    nombre = obtener_dato(lista_heroes, "nombre")
    if nombre:
        print(f"Nombre: {nombre}")


def obtener_nombre_y_dato(lista_heroes, clave):
    """
    Obtiene el nombre y un dato de un heroe.

    Parametros:
    heroe: heroe.
    clave: la clave del heroe.

    Devuelve:
    Un string con el nombre y el dato del heroe.
    """
  
    for heroe in lista_heroes:
        if clave in heroe:
            resultado = f"Nombre: {obtener_dato(heroe, 'nombre')} | Fuerza: {obtener_dato(heroe, clave)}"
            return resultado

 
    return False


def obtener_maximo(lista_heroes, clave):
    """
    Obtiene el valor maximo de una clave numerica en una lista de diccionarios

    Parametros:
    lista: Una lista de diccionarios que representan heroes
    clave: La clave obtiene el valor maximo

    Retorna:
        El valor maximo de la clave especificada
    """
    if not verificar_no_vacio(lista_heroes):
        return False

  
    normalizar_datos(lista_heroes)

    maximo = None  
    for heroe in lista_heroes:
        if maximo == None or heroe[clave] > maximo: 
            maximo = heroe[clave]
    return maximo


def obtener_minimo(lista_heroes, clave):
    """
    Obtiene el valor minimo de una clave numerica en una lista de lista_heroess

    Parametros:
    lista: Una lista de lista_heroes que representan heroes, donde algunas claves contienen datos numericos
    clave: La clave que se desea obtener el valor maximo

    Retorna:
        El valor minimo de la clave especificada o False si no se cumple la validacion
    """
    if not verificar_no_vacio(lista_heroes):
        return False


    normalizar_datos(lista_heroes)

    minimo = None 

    for heroe in lista_heroes:
        if minimo is None or heroe[clave] < minimo:
            minimo = heroe[clave]
    return minimo

    
def obtener_dato_cantidad(lista_heroes, valor, clave):
    """
    Obtiene una lista de heroes que cumplan con una condicion especifica en un dato ingredado

    Parametros:
    - lista_heroes: Una lista de diccionarios que representan heroes
    - valor: El valor que se debe buscar en el dato
    - clave: La clave que representa el dato en el que se buscara el valor

    Retorna:
    - Una lista de heroes que cumplen con la condición especificada en el dato

    """
    if not verificar_no_vacio(lista_heroes):
        return False


    normalizar_datos(lista_heroes)

    condicion = []

    for heroe in lista_heroes:
        if clave in heroe:
            heroe_valor = heroe[clave] 
            if heroe_valor == valor: 
                condicion.append(heroe)

    return condicion

    # Ejemplo de uso
    # mayor_altura = obtener_maximo(lista_personajes, "altura")
    # lista_heroes_max_altura = obtener_dato_cantidad(lista_personajes, mayor_altura, "altura")

    # for heroe in lista_heroes_max_altura:
    #     print(f"Nombre: {heroe['nombre']}, Altura: {heroe['altura']}")


def stark_imprimir_heroes(lista_heroes):
    """
    Recorre la lista y devuelve todo lo que hay en ella 
    
    """

    if not verificar_no_vacio:
        return False
    
    for heroe in lista_heroes:
        print("Heroe:")
        for clave, valor in heroe.items():
            print(f"{clave}: {valor}")
        print("\n")


def sumar_dato_heroe(lista_heroes, clave):
    """
    Suma los valores de una clave específica para cada heroe en una lista de heeroes.

    Parametros:
    - Una lista de diccionarios que representan heroes.
    - La clave que representa el dato que se desea sumar.

    Retorna:
    - La suma de los valores de la clave especificada para todos los héroes en la lista.

    
    """
    suma = 0

    if not verificar_no_vacio(lista_heroes):
        return False
    
    normalizar_datos(lista_heroes)
    
    for heroe in lista_heroes:
        if type(heroe) == dict and clave in heroe:
            valor = heroe[clave]

            # Verificamos si el valor es numérico (int o float)
            if type(valor) == int or type(valor) == float:
                suma += valor  # Sumamos el valor al total

    return suma


def dividir(dividendo, divisor):
    """
    Realiza la division entre dos numeros

    Parametros:
    - dividendo
    - divisor

    Retorna:
    - El resultado de la division si el divisor no es cero, o False si el divisor es cero
    """
    if divisor == 0:
        return False  
    
    resultado = dividendo / divisor  
    
    return resultado


def contar_heroes_con_dato(lista_heroes, clave):
    """
    Cuenta cuantos heroes en la lista tienen un dato especifico en la clave dada

    Parametros:
    - diccionario: Una lista de diccionarios que representan heroes
    - clave: La clave que representa el dato que se desea contar

    Retorna:
    - El numero de heroes que tienen el dato especifico en la clave dada
    """
    contador = 0 

    for heroe in lista_heroes:
        if clave in heroe:  
            contador += 1  

    return contador


def calcular_promedio(lista_heroes, clave):
    """
    Calcula el promedio

    Parametros:
    - lista_heroes: Una lista de diccionarios que representan heroes.
    - clave: La clave que representa el dato que se desea sumar.

    Retorna:
    - El promedio entre los valores de la lista
    """

    suma = sumar_dato_heroe(lista_heroes, clave)  
    cantidad_heroes = contar_heroes_con_dato(lista_heroes, clave)  

    if suma is False or cantidad_heroes == 0:
        return False

    promedio = dividir(suma, cantidad_heroes)  

    return promedio


def mostrar_promedio_dato(lista_heroes, clave):
    """
    Calcula el promedio.

    Parametros:
    - lista_heroes: Una lista de diccionarios que representan heroes.
    - clave: La clave que representa el dato que se desea sumar.

    Retorna:
    - El promedio entre los valores de la lista
    """
    if not verificar_no_vacio(lista_heroes):
        return False
    
    normalizar_datos(lista_heroes)

    promedio = calcular_promedio(lista_heroes , clave)

    if promedio != None:
        print(promedio)
    else:
        print("Error")


def imprimir_menu():
    """
    Imprime un menu
    """
    print("Eliga una opcion: \n",
        "1- Normalizar datos \n ",
        "2- Imprimir nombres de NB: \n ",
        "3- superhéroe mas alto del genero F: \n ",
        "4- superhéroe mas alto del genero M: \n ",
        "5- superhéroe mas debil del genero M: \n ",
        "6- superhéroe mas debil del genero NB: \n ",
        "7- fuerza promedio de los superhéroes de género NB: \n ",
        "8- cuántos superhéroes tienen cada tipo de color de ojos: \n,",
        "9- cuántos superhéroes tienen cada tipo de color de pelo: \n",
        "10- todos los superhéroes agrupados por color de ojos: \n",
        "11- todos los superhéroes agrupados por tipo de inteligencia: \n",
        "12- Salir: \n ",
        )


def validar_entero(valor):
    """
    Verifica si un string de numero está conformado unicamente por digitos

    Parametros:
    - valor: El string que se va a verificar

    Retorna:
    - True si el string está conformado unicamente por digitos, False en caso contrario

    """
    if valor.isdigit():
        return True
    else:
        return False


def stark_menu_principal():
    """
    Imprime un menu de opciones y valida la entrada del usuario.

    Retorna:
    - El numero de la opcion elegida como un entero, o False si la entrada no es valida.
    """

    imprimir_menu()
    
    while True:
        opcion = input("Ingrese una opcion del menu: ")

        if validar_entero(opcion):
            opcion_elejida_int = int(opcion)
            if (opcion_elejida_int >= 1 and opcion_elejida_int <= 12):
                return opcion_elejida_int
            else:
                print("Ingrese un numero del 1 al 12")
        else:
            print("Ingrese un numero valido")


def stark_marvel_app():
    """
    Funcion principal de la aplicación Stark Marvel

    Parametros:
    - lista_heroes: Una lista de diccionarios que representan cada heroe.
    """

    while True:
        opcion = stark_menu_principal()

        match(opcion):
            case 1:
                resultado = normalizar_datos(lista_personajes)
            case 2:
                resultado = mostrar_nombres_NB(lista_personajes)
            case 3:
                resultado = mostrar_superheroe_mas_alto_F(lista_personajes)
                print("Superhéroe más alto del género F:", resultado)

                print("\n")
            case 4:
                resultado = mostrar_superheroe_mas_alto_M(lista_personajes)
                print("Superhéroe más alto del género M:", resultado)

                print("\n")
            case 5:
                resultado = mostrar_superheroe_mas_debil_M(lista_personajes)
                print("Superhéroe más debil del género M:", resultado)
                print("\n")
            case 6:
                resultado = mostrar_superheroe_mas_debil_NB(lista_personajes)
                print("\n")
            case 7:
                resultado = mostrar_promedio_fuerza_NB(lista_personajes)
                print("\n")
            case 8:
                resultado = contar_colores_ojos(lista_personajes)
                print("cuántos superhéroes tienen cada tipo de color de ojos:", resultado)
                print("\n")
            case 9:
                resultado = contar_colores_pelo(lista_personajes)
                print("cuántos superhéroes tienen cada tipo de color de pelo:", resultado)
                print("\n")
            case 10:
                superheroes_por_color_ojos = listar_superheroes_por_color_ojos(lista_personajes)
                for color, superheroes in superheroes_por_color_ojos.items():
                    print(f"Color de Ojos: {color}")
                    print("Superhéroes:")
                    for heroe in superheroes:
                        print(f"Nombre: {heroe['nombre']}\n")  
            
            case 11:
                superheroes_por_inteligencia = listar_superheroes_por_inteligencia(lista_personajes)
                for inteligencia, superheroes in superheroes_por_inteligencia.items():
                    print(f"Inteligencia: {inteligencia}")
                    print(f"Superhéroes: ")
                    for heroe in superheroes:
                        print(f"Nombre: {heroe['nombre']}\n")     
                        if inteligencia == "":
                            print(f"Nombre: {heroe['nombre']} no tiene inteligencia definida \n")  
            
            case _:
                break

stark_marvel_app()







        


            
        


















