from data_stark import lista_personajes
import re
import json

#Camila Daraio

def extraer_iniciales(heroe, clave:str):
    """
    Muestra solo las iniciales de cada nombre
    Recibe: una lista con diccionarios

    """

    if clave in heroe:
        nombre = heroe[clave] 
        nombre = nombre.replace('-', '').replace('the', '') 
        palabras = nombre.split()  

        inicial_nombre = [] 
        for palabra in palabras:
            inicial = palabra[0].upper() 
            inicial_nombre.append(inicial)  

        iniciales_nombre = '.'.join(inicial_nombre) 
        
    return iniciales_nombre
    

def definir_iniciales_nombre(lista: list[dict]):
    """
    Parametros: La lista de diccionarios que representan héroes.
    
    Retorna: bool
    
    """
    for heroe in lista:
        if "nombre" not in heroe:
            return False

        iniciales = extraer_iniciales(heroe, "nombre") 
        heroe["iniciales"] = iniciales 

    return True
    

def agregar_iniciales_nombre(lista_heroes: list[dict]):
    """
    Agrega iniciales al nombre.
    """
    if type(lista_heroes) is list and len(lista_heroes)> 0:
                if definir_iniciales_nombre(lista_heroes) == False:
                    print("El origen de datos no contiene el formato correcto")
    return True 


agregar_iniciales_nombre(lista_personajes)

def stark_imprimir_nombres_con_iniciales(lista_heroes: list[dict]):
    """
    
    """
    definir_iniciales_nombre(lista_heroes)
    if type(lista_heroes) is list and len(lista_heroes) > 0:
        agregar_iniciales_nombre(lista_heroes)
        for heroe in lista_heroes:
            print(f"* {heroe['nombre']} {heroe['iniciales']}")
   

def generar_codigo_heroe(id_heroe, genero:str):
    """
     Genera el código de un héroe a partir de su identificador y género

    Recibe:
    id_heroe: El identificador numérico del heroe
    genero_heroe: El género del heroe

    Devuelve:
    el id del heroe o 'N/A' si hay errores de validación 
    
    """
    if genero != "M" and genero != "F" and genero != "NB":
        return "N/A"
    
    codigo_heroe = f"{genero}-{str(id_heroe).zfill(8)}"
    if len(codigo_heroe) > 10: 
        return "N/A"
    
    return codigo_heroe
    

def agregar_codigo_heroe(heroe , id_heroe):
    """
    Agrega el codigo generado a la lista basandose en su genero

    Recibe por parametro una lista y un id que representa un heroe

    Devuelve:
    -Un True si se agrego el codigo generado al diccionario
    -Un false en caso del que codigo generado contenga menos de 10 caracteres o la lista se encuentre
    
    """
    genero = heroe["genero"]
    codigo_heroe = generar_codigo_heroe(id_heroe, genero)
    heroe["codigo_heroe"] = codigo_heroe
    return True


def stark_generar_codigos_heroes(lista_heroes):
    """
    Genera e imprime los codigos en cada heroe
    
    """
    codigo_heroe = 1
    for heroe in lista_heroes:
        agregar_codigo_heroe(heroe, codigo_heroe)
        codigo_heroe += 1
    
    return f"El código del primer héroe es: {lista_heroes[0]['codigo_heroe']} \n" f"El código del primer héroe es: {lista_heroes[-1]['codigo_heroe']}"

 
stark_generar_codigos_heroes(lista_personajes)


def sanitizar_entero(numero_str):
    """
    analiza el string recibido y determinar si es un numero entero positivo.

    Devuelve:
    - Si es un numero entero lo devuelve casteado a int.
    - Si contiene carácteres no numéricos retornar -1
    - Si el número es negativo se deberá retornar un -2
    - Si ocurren otros errores que no permiten convertirlo a entero entonces se deberá retornar -3

    """

    
    numero_str = numero_str.strip()
    if numero_str.isdigit():  
        numero = int(numero_str)
        if numero >= 0:
            return numero  
        else:
            return -2  
    else:
        return -1  


def sanitizar_flotante(numero_str):
    """
    analiza el string recibido y determinar si es un número flotante.

    Devuelve:
    - Si es un numero flotante lo devuelve casteado a float.
    - Si contiene carácteres no numéricos retornar -1
    - Si el número es negativo se deberá retornar un -2
    - Si ocurren otros errores que no permiten convertirlo a entero entonces se deberá retornar -3

    """


    numero_str = numero_str.strip()
    if not numero_str.isalpha():  
        numero = float(numero_str)
        if numero >= 0:
            return numero 
        else:
            return -2  
    else:
        return -1  
    

def sanitizar_string(valor_str, valor_por_defecto='-'):
    """
    analiza el string recibido y determinar si es un str.
    """
    
    valor_str = valor_str.strip()

    valor_str = valor_str.replace("/", "") 

    if not valor_str.isdigit(): 
        valor_str = str(valor_str)
        return valor_str.lower()
    else:
        return 'N/A'


def sanitizar_dato(lista_heroes, clave, tipo_dato):
    """
    sanitiza el valor del diccionario correspondiente a la clave y al tipo de dato recibido

    """
    exito = False

    for heroe in lista_heroes: 
        if clave not in heroe: 
            print(f'La clave especificada no existe en el héroe')
            return False
        else:
            valor = heroe[clave] 

            if tipo_dato == "string":
                heroe[clave] = sanitizar_string(valor)
            elif tipo_dato == "entero":
                heroe[clave]= sanitizar_entero(valor)
            elif tipo_dato == "flotante":
                heroe[clave] = sanitizar_flotante(valor)
            exito = True

    return exito


def stark_normalizar_datos(lista_heroes):
    """
    Normaliza ciertos valores en la lista de héroes.
    
    Parametro:
        lista_heroes: Lista de héroes a normalizar.

    """
    if not lista_heroes:
        print("Error: Lista de héroes vacía")
        return
    

    sanitizar_dato(lista_heroes, "color_ojos", 'string')
    sanitizar_dato(lista_heroes, "color_pelo", 'string')
    sanitizar_dato(lista_heroes, "inteligencia", 'string')
    sanitizar_dato(lista_heroes, "fuerza", 'entero')
    sanitizar_dato(lista_heroes, "peso", 'flotante')
    sanitizar_dato(lista_heroes, "altura", 'flotante')

    print("Datos normalizados")


def generar_indice_nombres(lista_heroes):
    """
    Genera una lista con las palabras que componen los nombres de los personajes.

    Parametro:
    La lista de personajes

    Returna:
        Una lista de palabras que componen los nombres de los personajes.
    """

    if not lista_heroes:
        print("El origen de datos está vacío")
        return False

    indice_nombres = []
    for heroe in lista_heroes:
        if type(heroe) == dict and 'nombre' in heroe:
            nombre = heroe['nombre']
            palabras_nombre = nombre.split()
            indice_nombres.extend(palabras_nombre)
        else:
            print("El origen de datos no contiene el formato correcto para un personaje.")

    return indice_nombres


def stark_imprimir_indice_nombre(lista_heroes):
    """
    Muestra por pantalla el índice generado por la función generar_indice_nombres con guiones bajos entre cada palabra.
    
    Parametro:
    La lista de personajes

    """
    indice_nombres = generar_indice_nombres(lista_heroes)
    if indice_nombres:
        indice_str = '-'.join(indice_nombres)
        print(indice_str)
    else:
        print("No se pudo generar un índice de nombres.")


def convertir_cm_a_mtrs(valor_cm):
    """
    Convierte una medida en centímetros a metros.

    Parametro:
    - El valor en centímetros a convertir

    Retorna:
    - El valor convertido a metros o -1 si no es válido.

    """

    if type(valor_cm) == float and valor_cm >= 0:
        valor_mtrs = valor_cm / 100.0
        return valor_mtrs
    else:
        return -1 
    

def generar_separador(patron:str, largo:int, imprimir=True):
    """
    Genera un separador con el patron especificado y longitud dada

    Parametro:
    - Patron: El caracter o patrón a utilizar en el separador.
    - Largo: La longitud del separador.
    - Imprimir: Si es True, imprimira el separador por pantalla.

    Retorna:
        El separador generado o N/A si las validaciones no se cumplen

    """


    if not type(largo) == int or not 1 <= largo <= 235:
        return 'N/A'


    separador = patron * largo

    return separador


def generar_encabezado(titulo):
    """
    Genera un encabezado con el titulo en mayusculas envuelto entre separadores.

    """
    titulo = titulo.upper()

    separador = generar_separador("*", 50, True)


    encabezado = f"{separador}\n{titulo}\n{separador}"

    return encabezado


def imprimir_ficha_heroe(heroe):
    """
    Imprime la ficha de un heroe en el formato especificado.

    Parametros:
        heroe: Un diccionario con los datos del heroe.

    Retorna:
        None
    """

    encabezado_principal = generar_encabezado("Principal")

    nombre_heroe = heroe["nombre"] 
    iniciales = heroe["iniciales"]
    identidad_secreta = heroe["identidad"]
    empresa = heroe["empresa"]
    codigo_heroe = heroe["codigo_heroe"]


    encabezado_fisico = generar_encabezado("Físico")

    altura = convertir_cm_a_mtrs(heroe['altura'])

    peso = heroe["peso"]
    fuerza = heroe["fuerza"]


    encabezado_senas_particulares = generar_encabezado("Señas Particulares")


    color_ojos = heroe["color_ojos"]
    color_pelo = heroe["color_pelo"]

    print(encabezado_principal)
    print(f"NOMBRE DEL HÉROE: {nombre_heroe} ({iniciales})")
    print(f"IDENTIDAD SECRETA: {identidad_secreta}")
    print(f"EMPRESA: {empresa}")
    print(f"CÓDIGO DE HÉROE: {codigo_heroe}")
    print(encabezado_fisico)
    print(f"ALTURA: {altura} Mtrs.")
    print(f"PESO: {peso} Kg.")
    print(f"FUERZA: {fuerza} N")
    print(encabezado_senas_particulares)
    print(f"COLOR DE OJOS: {color_ojos}")
    print(f"COLOR DE PELO: {color_pelo}")


def stark_navegar_fichas(lista_heroes):
    """
    Parametro:
    - Lista de heroes.

    """
    if not lista_heroes:
        print("Error: Lista de héroes vacía")
        return

    indice_actual = 0

    while True:
        imprimir_ficha_heroe(lista_heroes[indice_actual])

        print("\n[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            indice_actual -= 1
            if indice_actual < 0:
                indice_actual = len(lista_heroes) - 1 
        elif opcion == "2":
            indice_actual += 1
            if indice_actual >= len(lista_heroes):
                indice_actual = 0 
        elif opcion.lower() == "s":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def imprimir_menu():
    """
    Imprime un menu.

    """
    while True:
        print(
        "1 - Imprimir la lista de nombres junto con sus iniciales \n",
        "2 - Generar códigos de héroes \n",
        "3 - Normalizar datos \n",
        "4 - Imprimir índice de nombres \n",
        "5 - Navegar fichas \n",
        "6 - Salir \n",
        )
        break


def stark_menu_principal():
    """
    Imprime un menu de opciones y valida la entrada del usuario.

    Retorna:
    - El numero de la opcion elegida como un entero, o False si la entrada no es valida.
    """

    imprimir_menu()
    
    while True:
        opcion = input("Ingrese una opcion del menu: ")

        opcion_elejida_int = int(opcion)
        if (opcion_elejida_int >= 1 and opcion_elejida_int <= 6):
                print("numero correcto")
                return opcion_elejida_int
        else:
            print("Ingrese un numero valido")


def stark_marvel_app_3(lista_heroes):
    """
    
    """

    while True:
        opcion = stark_menu_principal()

        match opcion:
            case 1:
                stark_imprimir_nombres_con_iniciales(lista_heroes)
            case 2:
                stark_generar_codigos_heroes(lista_heroes)
                print(f"El código del primer héroe es: {lista_heroes[0]['codigo_heroe']}") 
                print(f"El código del primer héroe es: {lista_heroes[-1]['codigo_heroe']}")               
            case 3:
                stark_normalizar_datos(lista_heroes)
                print(lista_personajes)
            case 4:
                stark_imprimir_indice_nombre(lista_heroes)
            case 5:
                stark_navegar_fichas(lista_heroes)
            case _:
                break


stark_marvel_app_3(lista_personajes)


