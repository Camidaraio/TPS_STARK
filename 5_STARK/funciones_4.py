from data_stark import lista_personajes
import re

# 
# Camila Daraio
# DESAFIO STARK 4

def extraer_iniciales(nombre_heroe:str)->str:
    '''Recibe un nombre y devuelve sus iniciales en mayusculas separas por un ".", si el nombre contiene "the" lo omite.'''

    if len(nombre_heroe) == 0:
        return 'N/A'

    palabras = nombre_heroe.split()

    lista_iniciales = []

    for palabra in palabras:

        if palabra.lower() == 'the':
            continue

        palabra = palabra.replace('-', ' ')

        inicial = palabra[0].upper()

        lista_iniciales.append(inicial)

    salida = '.'.join(lista_iniciales)

    return salida

# print(extraer_iniciales("Howard the Duck asdeee"))

def definir_iniciales_nombre(heroe:dict):
    '''Recibe un diccionario evalua q no sea un diccionario y q contenga la clave "nombre". Luego agrega le agrega la clave "iniciales" ejecutando la funcion "extraer_iniciales"'''

    if type(heroe) != dict or 'nombre' not in heroe:
        return False

    heroe["iniciales"] = extraer_iniciales(heroe["nombre"])

    return True

# heroe = definir_iniciales_nombre(lista_personajes[6])
# print(heroe)

def agregar_iniciales_nombre(lista_heroes:list):
    '''Recibe una lista, valida que no esta vacia y que sea de tipo lista. Luego a cada diccionario le agrega el valor "iniciales" ejecutando la funcion "definir_iniciales_nombre". Devuelve un Boolean'''

    if len(lista_heroes) == 0 or type(lista_heroes) != list:
        retorno = False

    for heroe in lista_heroes:
        if definir_iniciales_nombre(heroe) == False:
            print('El origen de datos no contiene el formato correcto')
            retorno = False
        else:
            definir_iniciales_nombre(heroe)
            retorno = True
    return retorno

# print(agregar_iniciales_nombre(lista_personajes))
# for heroe in lista_personajes:
#     print(heroe['nombre'])
#     for clave, valor in heroe.items():
#         if clave == 'iniciales':
#             print(f'\n{clave}: {valor}\n')


def stark_imprimir_nombres_con_iniciales(lista_heroes:list)->str or False:
    '''Recibe una lista, agrega iniciales e imprime una cadena de string con las inciales. Si la lista esta vacia o en parametro no es una lista deuelve "False"'''

    if len(lista_heroes) == 0 or type(lista_heroes) != list:
        retorno = False

    agregar_iniciales_nombre(lista_heroes)
    for heroe in lista_heroes:
        print(f"* {heroe['nombre']} ({heroe['iniciales']})")

# stark_imprimir_nombres_con_iniciales(lista_personajes)

def generar_codigo_heroe(id_heroe:int, genero_heroe:str):
    '''Recibe un id y un genero por parametro'''
    retorno = False
    if type(id_heroe) == int and genero_heroe == "M" or genero_heroe == "F" or genero_heroe == "NB":
        retorno = f"{genero_heroe}-{id_heroe:010}"
    return retorno

# print(generar_codigo_heroe(12, "M"))
# print(generar_codigo_heroe(1, "F"))
# print(generar_codigo_heroe(223, "NB"))

def agregar_codigo_heroe(heroe:dict, id_heroe:int)->bool:
    '''Recine un diccionario y un id, utilizando la funcion "generar_codigo_heroe" se agrega el codigo como valor de la clave "codigo_heroe".Previamente valida que la cantidad de numeros del codigo sean 10.'''

    retorno = False

    if len(heroe) != 0:

        codigo = generar_codigo_heroe(id_heroe, heroe["genero"])

        # chequear minusculas, estan al pedo
        # chequear minusculas, estan al pedo

        codigo_a_validar =  re.sub(r'[a-zA-Z-]','', codigo)

        if len(codigo_a_validar) == 10:
            heroe['codigo_heroe'] = codigo
            retorno = True

    return retorno

# print(agregar_codigo_heroe(lista_personajes[23], 8))

def stark_generar_codigos_heroes(lista_heroes:list):
    '''Ejecuta "agregar_codigo_heroe". Printea cuandos codigos se asignaron, e imprime detalle de heroes con sus codigos. Tambien informa en caso de que algun diccionario no posea clave "codigo_heroe"'''

    if len(lista_heroes) != 0:

        contador = 0

        for indice in range(len(lista_heroes)):
            if type(lista_heroes[indice]) == dict and 'genero' in lista_heroes[indice]:
                bool_agrega_codigo = agregar_codigo_heroe(lista_heroes[indice], indice+1)
                if bool_agrega_codigo:
                    contador += 1

        print(f"Se asignaron {contador} codigos")
        for heroe in lista_heroes:
            if 'codigo_heroe' in heroe:
                print(f"* El código del héroe {heroe['nombre']} es: {heroe['codigo_heroe']}")
            else:
                print(f"* El heroe {heroe['nombre']} no posee clave 'codigo_heroe'")

# stark_generar_codigos_heroes(lista_personajes)

# 3.1
def sanitizar_entero(numero_str:str):
    '''Recibe un numero en formato STR y lo devuelve entero. De no ser entero retonar "-3"'''
    retorno = -3


    if type(numero_str) == str:
        numero_str = numero_str.strip()

        if re.search(r'[^0-9-]', numero_str) or numero_str == '':
            retorno = -1
        elif int(numero_str) < 0:
            retorno = -2
        else:
            retorno = int(numero_str)

    return retorno