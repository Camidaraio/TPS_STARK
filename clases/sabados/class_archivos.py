import re
#Archivos

#"w": abro el archivo en modo texto. si ya existe texto lo pisa

# archivo = open("mi_archivo", "w" )

# archivo.write("Hola, buenos dias mundo ")
# archivo.close() #cerramos el archivo. siempre se cierra porque se pueda romper el archivo

#----------------------------------

#"a": anexa informacion

# archivo = open("mi_archivo", "a" )

# archivo.write("como estas?")
# archivo.close() #cerramos el archivo. siempre se cierra porque se pueda romper el archivo

#----------------------------------

#with hace que el archivo que estoy creando no hace falta que cierre el archivo ya que el with lo hace aumaticamente
# as: significa como.  Aquello que abre el open lo va a reconocer como la variable archivo

# lista = ["pepe", "maria", "luis"]
# with open("mi_archivo.txt", "w") as archivo:
#     for nombre in lista:
#         archivo.write(f"{nombre}\n") 

#----------------------------------

# #r: 
# lista=[]
# archivo = open("mi_archivo.txt", "r")
# lista = archivo.readlines()
# for  nombre in archivo:
#     lista.append(nombre)


# print(lista)
# # with
# lista=[]
# with open("mi_archivo.txt", "r") as archivo:
#     lista = archivo.readlines()
#     for  nombre in archivo:
#         lista.append(nombre)


#     print(lista)

#----------------------------------


deescripciones  = ["coca", "pepsi", "mirinda"]
precios = [799,82, 642.21, 605.66]
stock = [5,4,8]

# with open("producctos.csv", "w") as archivo:
#     for i in range(len(stock)):
#         producto_str = f"{deescripciones[i]},{precios[i]},{stock[i]}\n"
#         archivo.write(producto_str)


#----------------------------------


# with open("producctos.csv", "r") as archivo:
#     for linea in archivo:
#         print(linea, end="") #el end lo acomoda uno al lado del otro

# with open("producctos.csv", "r") as archivo:
#     for linea in archivo:
#        registro = re.split(",|\n",linea )
#        print(f"{registro[0]}--{registro[1]}--{registro[2]}")

#----------------------------------

def parser_productos(path:str) -> list:
    lista = []

    with open("producctos.csv", "r") as archivo:
        for linea in archivo:
            registro = re.split(",|\n",linea )
            producto = {}
            producto["descripcion"] = registro[0]
            producto["precios"] = float(registro[1])
            producto["stock"] = int(registro[2])
            lista.append(producto)

    # for producto in lista:
    #     print(f"{producto["descripcion"]:15} {producto["precios"]:15} {producto["stock"]:15}  ")

