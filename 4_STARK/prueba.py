from data_stark import lista_personajes
from tp4_1 import *

#------- punto 1.0 -----

# nombre = extraer_iniciales(lista_personajes, "nombre")
# print(nombre)

#------- punto 1.2 -----
# resultado = definir_iniciales_nombre(lista_personajes)

# # Verificar si se agregaron las iniciales correctamente
# if resultado:
#     for heroe in lista_personajes:
#         print(f"Nombre: {heroe['nombre']}, Iniciales: {heroe['iniciales']}")
# else:
#     print("No se pudieron agregar las iniciales.")

#--------------- punto 1.3 ---------------

# stark_imprimir_nombres_con_iniciales(lista_personajes)

#--------------- punto 2.1 ---------------

# codigo_heroe = generar_codigo_heroe(1, "M")
# print(codigo_heroe)

#--------------- punto 2.2 ---------------

# agregar_codigo_heroe(lista_personajes, 6)
# print(lista_personajes)

#--------------- punto 2.3 ---------------


# stark_generar_codigos_heroes(lista_personajes)

#--------------- punto 3.1 ---------------

# numero_str = "6"
# resultado = sanitizar_entero(numero_str)
# print(resultado)


#--------------- punto 3.3 ---------------
# numero_str = "s/JJHH"
# resultado = sanitizar_string(numero_str)
# print(resultado)

#--------------- punto 3.4 ---------------

# exito = sanitizar_dato(lista_personajes, "fuerza", "entero")

# # Verificar si al menos un héroe fue sanitizado con éxito
# if exito:
#     print("Al menos un héroe fue sanitizado con éxito.")
#     print(lista_personajes)
# else:
#     print("Ningún héroe fue sanitizado.")

#--------------- punto 3.5 ---------------

# stark_normalizar_datos(lista_personajes)
# print(lista_personajes)

#--------------- punto 4.2 ---------------

#nombre = stark_imprimir_indice_nombre(lista_personajes)

#--------------- punto 5.1 ---------------


# valor_cm = 150  # Reemplaza con tu valor en centímetros
# valor_convertido = convertir_cm_a_mtrs(valor_cm)
# if valor_convertido != -1:
#     print(f"{valor_cm} centímetros es igual a {valor_convertido} metros.")
# else:
#     print("El valor ingresado no es válido.")

#--------------- punto 5.2 ---------------
# separador = generar_separador('*', 10)

#--------------- punto 5.3 ---------------

# titulo = "Principal"
# encabezado = generar_encabezado(titulo)
# print(encabezado)

#--------------- punto 5.4 ---------------

#imprimir_ficha_heroe(lista_personajes[0])


#--------------- punto 5.5 ---------------

# stark_navegar_fichas(lista_personajes)

#--------------- punto 6.1 ---------------
# print(imprimir_menu())

#--------------- punto 6.2 ---------------

# stark_menu_principal()

#--------------- punto 5.5 ---------------

# imprimir_ficha_heroe(lista_personajes)

#--------------- punto 6.3 ---------------


stark_marvel_app_3(lista_personajes)


#punto 2

# def generar_codigo_heroe(id_heroe, genero):
#     """
#     Genera el código de un héroe a partir de su identificador y género

#     Recibe:
#     id_heroe (int): El identificador numérico del héroe.
#     genero_heroe (str): El género del héroe.

#     Devuelve:
#     el id del heroe o 'N/A' si hay errores de validación .

#     """
#     # Validacion
#     if not type(id_heroe) == int:
#         print("El identificador del héroe no es numérico.")
#         return 'N/A'

#     if genero != "M" and  genero != "F" and genero != "NB":
#         print("El género no es válido. Debe ser 'M', 'F' o 'NB'.")
#         return 'N/A'


#     codigo_heroe = f"{genero}-{str(id_heroe).zfill(8)}"
#     if len(codigo_heroe) > 10: 
#         return "N/A"

#     return codigo_heroe


# def agregar_codigo_heroe(lista_heroes, id_heroe):
#     """
#     Agrega el codigo generado a la lista basandose en su genero
#     Recibe por parametro una lista y un id que representa un heroe
#     Devuelve:
#     -Un True si se agrego el codigo generado al diccionario
#     -Un false en caso del que codigo generado contenga menos de 10 caracteres o la lista se encuentre
#     """
#     if not lista_heroes:
#         print("Lista vacía")
#         return False
    
    
#     for heroe in lista_heroes:
#         genero = heroe["genero"]
#         codigo = generar_codigo_heroe(id_heroe, genero)
#         heroe["codigo_heroe"] = codigo
#         return True    


#     # if len(codigo) > 10:
#     #     print("El codigo generado no tiene 10 caracteres")
#     #     return False

    


# def stark_generar_codigos_heroes(lista_heroes):
#     """
    
#     """
#     if not lista_heroes:
#         print("Lista vacía")
#         return False
    
#     if not type(lista_heroes) == list:
#         print("El origen de datos no contiene el formato correcto")
#         return False
    
#     for heroe in lista_heroes:
#         if 'genero' not in heroe:
#             print("Falta la clave 'genero' en uno o más diccionarios.")
#             return
        

#     contador = 1
#     for heroe in lista_heroes:
#         agregar_codigo_heroe(lista_heroes, contador)
#         contador += 1
 
#     print(f"El código del primer héroe es: {lista_heroes[0]['codigo_heroe']}")
#     print(f"El código del primer héroe es: {lista_heroes[-1]['codigo_heroe']}")
