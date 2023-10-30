# from funciones import *

# lista_usuarios = [
#     {"nombre_usuario": "Juan", "contraseña": "Clave123"},
#     {"nombre_usuario": "Maria", "contraseña": "Contraseña456"},
#     {"nombre_usuario": "Pedro", "contraseña": "Pass789"},
#     {"nombre_usuario": "Laura", "contraseña": "Secreto101"},
#     {"nombre_usuario": "Carlos", "contraseña": "Contraseña2023"}

# ]

# # mostrar_usuarios(lista_usuarios)

# # nuevo = {"nombre_usuario": "Pepito", "contraseña": "123"}

# mostrar_usuarios(lista_usuarios)

# while True:
#     opcion = input("1. Cargar\n2. Mostrar\3. Eliminar\n4. Insertar\n5. Vaciar\n6. Salir")
#     match opcion:
#         case "1":
#             cargar_usuarios(lista_usuarios)
#         case "2":
#             if len(lista_usuarios):
#                 mostrar_usuarios(lista_usuarios)
#             else:
#                 print("La lista está vacía")
#         case "3":
            
#             nombre = input("Ingrese usuario: ")

#             encontro =  eliminar_usuario(lista_usuarios, nombre)

#             if encontro != None:
#                 print("Usuario eliminado: ")    
#                 # mostrar_usuarios(lista_usuarios)
#             else:
#                 print("Usuario no encontrado o contraseña inválida")

#         case "4":
#             nuevo = pedir_usuario()

#             lista_usuarios.insert(1, nuevo)
#         case "5":
#             lista_usuarios.clear()
#         case "6":
#             break