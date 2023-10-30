from data_stark import lista_personajes

#Nombre: Franco
#Apellido: Dominguez
#Trabajo: Desafio Stark 04

"""
Desafío #04:
IMPORTANTE: Para todas y cada una de las funciones creadas, documentarlas
escribiendo que es lo que hacen, que son los parámetros que reciben (si es una lista,
un string, etc y que contendrá) y que es lo que retorna la función!

1.1. Crear la función ‘extraer_iniciales’ que recibirá como parámetro:
● nombre_heroe: un string con el nombre del personaje
La función deberá devolver a partir del parámetro recibido un nuevo string con
las iniciales del nombre del personaje seguidos por un punto (.)
● En el caso que el nombre del personaje contenga el artículo ‘the’ se
deberá omitir de las iniciales
● Se deberá verificar si el nombre contiene un guión ‘-’ y sólo en el caso
que lo tenga se deberá reemplazar por un espacio en blanco
La función deberá validar:
● Que el string recibido no se encuentre vacío
Devolver ‘N/A’ en caso de no cumplirse la validación

Ejemplo de la salida de la función para Howard the Duck:
H.D.

1.2. Crear la función ‘definir_iniciales_nombre’ la cual recibirá como parámetro:
● heroe: un diccionario con los datos del personaje

La función deberá agregar una nueva clave al diccionario recibido como
parámetro. La clave se deberá llamar ‘iniciales’ y su valor será el obtenido de
llamar a la función ‘extraer_iniciales’
La función deberá validar:
● Que el dato recibido sea del tipo diccionario
● Que el diccionario contengan la clave ‘nombre’
En caso de encontrar algún error retornar False, caso contrario retornar True

1.3. Crear la función ‘agregar_iniciales_nombre’ la cual recibirá como
parámetro:
● lista_heroes: lista de personajes
Se deberá validar:
● Que lista_heroes sea del tipo lista
● Que la lista contenga al menos un elemento
La función deberá iterar la lista_heroes pasándole cada héroe a la función
definir_iniciales_nombre.
En caso que la función definir_iniciales_nombre() retorne False entonces se
deberá detener la iteración e informar por pantalla el siguiente mensaje:
‘El origen de datos no contiene el formato correcto’
La función deberá devolver True en caso de haber finalizado con éxito o False
en caso de que haya ocurrido un error

1.3. Crear la función ‘stark_imprimir_nombres_con_iniciales’ la cual recibirá
como parámetro:
● lista_heroes: la lista de personajes
La función deberá utilizar la función agregar_iniciales_nombre’ para añadirle
las iniciales a los diccionarios contenidos en la lista_heroes
Luego deberá imprimir la lista completa de los nombres de los personajes
seguido de las iniciales encerradas entre paréntesis ()
Se deberá validar:
● Que lista_heroes sea del tipo lista
● Que la lista contenga al menos un elemento
Delante de cada nombre se deberá agregar un asterisco ‘*’ (de forma de
viñeta) seguido de un espacio.
Ejemplo de salida:
* Howard the Duck (H.D.)
* Rocket Raccoon (R.R.)
...
La función no retorna nada

"""
#1.1
def extraer_iniciales(nombre_heroe = str):
    iniciales_heroe = []

    if not nombre_heroe:
        return "N/A"

    nombre = nombre_heroe.replace("the", "").split()
    

    for palabra in nombre:
        palabra = palabra.replace("-", "")
        inicial = palabra[0]
        iniciales_heroe.append(inicial)




    return".".join(iniciales_heroe)


# 1.2

def definir_iniciales_nombre(heroe : dict):

    if type(heroe) != dict:
        return False

    if "nombre" not in heroe:
        return False

    heroe["iniciales"] = extraer_iniciales(heroe["nombre"])
    return True


#1.3
def agregar_iniciales_nombre(lista_heroes : list):

    if type(lista_heroes) != list or not lista_heroes:
        print("Error, la lista se encuentra vacia, o no es una lista")
    
    for heroe in lista_heroes:
        if not definir_iniciales_nombre(heroe):
            print("El origen de datos no contiene el formato correcto")
            return False

    return True
    


#1.3
def stark_imprimir_nombres_con_iniciales(lista_heroes : list):

    if type(lista_heroes) != list or not lista_heroes or not agregar_iniciales_nombre(lista_heroes):
        print("Error, la lista se encuentra vacia, o no es una lista")


    for heroe in lista_heroes:
        
        if "nombre" in heroe and "iniciales" in heroe:
            nombre = heroe["nombre"]
            iniciales = heroe["iniciales"]
            print(f"* {nombre} ({iniciales})")
        
        
#2.1
def generar_codigo_heroe(id_heroe, genero_heroe : str):
    if genero_heroe != "M" and genero_heroe != "F" and genero_heroe != "NB":
        return "N/A"
    
    codigo_heroe = f"{genero_heroe}-{str(id_heroe).zfill(8)}"
    if len(codigo_heroe) > 10: 
        return "N/A"
    
    return codigo_heroe
      
#2.2
def agregar_codigo_heroe(heroe , id_heroe):

    genero_heroe = heroe["genero"]
    codigo_heroe = generar_codigo_heroe(id_heroe, genero_heroe)
    heroe["codigo_heroe"] = codigo_heroe
    return True


#2.3
def stark_generar_codigos_heroes(lista_heroes : list):
    codigo_heroe = 1
    for heroe in lista_heroes:
        agregar_codigo_heroe(heroe, codigo_heroe)
        codigo_heroe += 1
    
    return f"El código del primer héroe es: {lista_heroes[0]['codigo_heroe']}\n" f"El código del primer héroe es: {lista_heroes[-1]['codigo_heroe']}"


stark_generar_codigos_heroes(lista_personajes)

# #3.1
def sanitizar_entero(numero_str):
    # numero_str = numero_str.strip()

    # if not numero_str:
    #     return -3
    
    # if not numero_str.isdigit():
    #     return -1
    
    # numero_entero = int(numero_str)

    # if numero_entero < 0:
    #     return -2
    

    # return numero_entero
    numero_str = numero_str.strip()
    if numero_str.isdigit():
        numero = int(numero_str)
        if numero >= 0:
            return numero
        else:
            return -2
    else:
        return -1

#3.2
def sanitizar_flotante(numero_str):
    
    if not numero_str:
        return -3

    numero_str = numero_str.strip()
    if not numero_str.isalpha():
        numero = float(numero_str)
        if numero >= 0:
            return numero 
        else:
            return -2
    else:
        return -1

#3.3
def sanitizar_string(valor_str, valor_por_defecto='-'):
    
    # valor_str = valor_str.strip()
    # valor_por_defecto = valor_por_defecto.strip()

    
    # valor_str = valor_str.replace('/', ' ')

   
    # contiene_numeros = False
    # for char in valor_str:
    #     if char.isdigit():
    #         contiene_numeros = True
    #         break  

    # if contiene_numeros:
    #     return "N/A"

    
    # if not valor_str and valor_por_defecto:
    #     return valor_por_defecto.lower()

   
    # return valor_str.lower()
    valor_str = valor_str.strip()

    valor_str = valor_str.replace("/", "") 

    if not valor_str.isdigit(): 
        valor_str = str(valor_str)
        return valor_str.lower()
    else:
        return 'N/A'

#3.4
def sanitizar_dato(lista_heroes, clave, tipo_dato):

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
  
    

#3.5
def stark_normalizar_datos(lista_heroes):
    """
    Normaliza ciertos valores en la lista de héroes.
    
    Args:
        lista_heroes (list): Lista de héroes (diccionarios) a normalizar.
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


#4.1
def generar_indice_nombres(lista_heroes):
    
    if not lista_heroes:
        print("El origen de datos no contiene el formato correcto")
        return []

    
    for heroe in lista_heroes:
        if not type(heroe) == dict:
            print("El origen de datos no contiene el formato correcto")
            return []

    
    for heroe in lista_heroes:
        if 'nombre' not in heroe:
            print("El origen de datos no contiene el formato correcto")
            return []

    
    nombres = []
    for heroe in lista_heroes:
        nombre = heroe['nombre']
        palabras = nombre.split()
        nombres.extend(palabras)

    return nombres

#4.2
def stark_imprimir_indice_nombre(lista_heroes):
    
    indice_nombres = generar_indice_nombres(lista_heroes)

    
    indice = '-'.join(indice_nombres)
    print(indice)

#5.1
def convertir_cm_a_mtrs(valor_cm):
    
    if type(valor_cm) not in [int, float] or valor_cm < 0:
        return -1

    
    valor_mtrs = valor_cm / 100.0

    return valor_mtrs

#5.2
def generar_separador(patron, largo, imprimir=True):
    
    if not (1 <= len(patron) <= 2):
        return 'N/A'

    
    if not (type(largo) == int and 1 <= largo <= 235):
        return 'N/A'

    
    separador = patron * largo

    
    if imprimir:
        print(separador)

    
    return separador

#5.3
def generar_encabezado(titulo):
    
    titulo = titulo.upper()

    
    largo_separador = 80  

    
    separador_superior = '*' * largo_separador

    
    separador_inferior = '*' * largo_separador

    
    encabezado = f"{separador_superior}\n{titulo}\n{separador_inferior}"

    return encabezado

#5.4
def imprimir_ficha_heroe(heroe):
    
    encabezado_principal = generar_encabezado("Principal")

    
    nombre_heroe = heroe.get("nombre", "")
    identidad = heroe.get("identidad", "")
    empresa = heroe.get("empresa", "")
    codigo_heroe = heroe.get("codigo_heroe", "")

    
    encabezado_fisico = generar_encabezado("Físico")

    
    altura = heroe.get("altura", "")
    peso = heroe.get("peso", "")
    fuerza = heroe.get("fuerza", "")

    
    encabezado_senas_particulares = generar_encabezado("Señas Particulares")

    
    color_ojos = heroe.get("color_ojos", "")
    color_pelo = heroe.get("color_pelo", "")

    
    ficha_heroe = f"{encabezado_principal}\n"
    ficha_heroe += f"NOMBRE DEL HÉROE: {nombre_heroe}\n"
    ficha_heroe += f"IDENTIDAD: {identidad}\n"
    ficha_heroe += f"EMPRESA: {empresa}\n"
    ficha_heroe += f"CÓDIGO DE HÉROE : {codigo_heroe}\n"
    ficha_heroe += f"{encabezado_fisico}\n"
    ficha_heroe += f"ALTURA: {altura} Mtrs.\n"
    ficha_heroe += f"PESO: {peso} Kg.\n"
    ficha_heroe += f"FUERZA: {fuerza} N\n"
    ficha_heroe += f"{encabezado_senas_particulares}\n"
    ficha_heroe += f"COLOR DE OJOS: {color_ojos}\n"
    ficha_heroe += f"COLOR DE PELO: {color_pelo}\n"

    
    print(ficha_heroe)

#5.5
def stark_navegar_fichas(lista_heroes):
    
    if not lista_heroes:
        print("Error: Lista de héroes vacía")
        return

    
    indice_actual = 0

    while True:
        
        heroe_actual = lista_heroes[indice_actual]

       
        imprimir_ficha_heroe(heroe_actual)

        
        opcion = input("Ingrese una opción: [1] Izquierda, [2] Derecha, [S] Salir: ").strip().upper()

        if opcion == '1':
            
            if indice_actual == 0:
                indice_actual = len(lista_heroes) - 1
            else:
                indice_actual -= 1
        elif opcion == '2':
            
            if indice_actual == len(lista_heroes) - 1:
                indice_actual = 0
            else:
                indice_actual += 1
        elif opcion == 'S':
            
            break
        else:
            
            print("Opción inválida. Ingrese una opción válida.")

#6.1
def imprimir_menu():
    print("1 - Imprimir la lista de nombres junto con sus iniciales")
    print("2 - Generar códigos de héroes")
    print("3 - Normalizar datos")
    print("4 - Imprimir índice de nombres")
    print("5 - Navegar fichas")
    print("S - Salir")
    print("_" * 60)

#6.2
def stark_menu_principal():
    imprimir_menu()  

    while True:
        opcion = input("Ingrese una opción: ").strip().upper()

        if opcion in ["1", "2", "3", "4", "5", "S"]:
            return opcion  
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

#6.3
def stark_marvel_app_3(lista_heroes):
    while True:
        opcion = stark_menu_principal()  

        if opcion == "1":
            stark_imprimir_nombres_con_iniciales(lista_heroes)
        elif opcion == "2":
            stark_generar_codigos_heroes(lista_heroes)
            print(f"El código del primer héroe es: {lista_heroes[0]['codigo_heroe']}") 
            print(f"El código del primer héroe es: {lista_heroes[-1]['codigo_heroe']}")
        elif opcion == "3":
            stark_normalizar_datos(lista_heroes)
            print(lista_heroes)
        elif opcion == "4":
            stark_imprimir_indice_nombre(lista_heroes)
        elif opcion == "5":
            stark_navegar_fichas(lista_heroes)
        elif opcion == "S":
            print("¡Hasta luego!")
            break
        else:
            print("Opción incorrecta. Por favor, elija una opción válida.")
    

# stark_marvel_app_3(lista_personajes)

stark_normalizar_datos(lista_personajes)
print(lista_personajes)
