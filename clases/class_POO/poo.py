
# ------ POO -------------
# class personaje():
#     """
#     Se puede documentar
#     """
#     tipo = "Hola" #Atributo de clase
#     def __init__(self, nombre="") -> None:
#         self.nombre = nombre

#     def mostrar(self):
#         print(self.nombre)


# aux_personaje1 = personaje()
# aux_personaje2 = personaje("Juana")
# aux_personaje1.mostrar()
# aux_personaje2.mostrar()

#En este caso los tres me muestras la variable q defini arriba como tipo, que es una atributo de clase.
 
# print(aux_personaje1.tipo)
# print(aux_personaje2.tipo)
# print(personaje.tipo)

# -------- Atributos protegidos-----

#Se proteje poniend __ antes del .
# Ejemplo: aux_personaje2.__nombre 

# class personaje():
#     """
#     Se puede documentar
#     """
#     tipo = "Hola" #Atributo de clase
#     def __init__(self, nombre="") -> None:
#         self.nombre = nombre

#     def mostrar(self):
#         print(self.nombre)

# aux_personaje1 = personaje()
# aux_personaje2 = personaje("Juana")
# aux_personaje2.__nombre = ("Juana")

# aux_personaje1.mostrar()
# aux_personaje2.mostrar()


# -------- Property -------

#existen los getters o setters

#---- getter----

# class personaje():
#     """
#     Se puede documentar
#     """

#     def __init__(self, nombre="") -> None:
#         self.__nombre = nombre #Variable privada

#     @property #Getter
#     def nombre(self): 
#         return self.__nombre
    
#     def set_nombre(self, nombre): 
#         self.__nombre = nombre


# aux= personaje("vero")
# print(aux.nombre)
# aux.nombre = "Juana"


#--- setter---

# class personaje():
#     """
#     Se puede documentar
#     """

#     def __init__(self, nombre="") -> None:
#         self.__nombre = nombre #Variable privada
#         self.apellido = ""

#     @property #Getter
#     def nombre(self): 
#         return self.__nombre
    
#     @nombre.setter #setter
#     def nombre(self, nombre): 
#         self.__nombre = nombre


# aux = personaje("Vero")
# print(aux.nombre)
# aux.nombre = "Camila"
# aux.apellido = "Daraio"
# print(aux.nombre)

#---  Metodos dunder ---

#Sobre carga de operador: str. contains, len,getitem, iter, etc 

#Hay varios metedos

# class personaje():
#     """
#     Se puede documentar
#     """

#     def __init__(self, nombre="") -> None:
#         self.__nombre = nombre #Variable privada
#         self.apellido = ""
#         self.lista = range(10)

#     @property #Getter
#     def nombre(self): 
#         return self.__nombre
    
#     @nombre.setter #setter
#     def nombre(self, nombre): 
#         self.__nombre = nombre


#     def __str__(self) -> str: #Convierte el objeto a str
#         return self.__nombre + " HOLA"
    
#     def __len__(self):
#         return 8
    
#     def __getitem__(self, index):
#         if (index == "nombre"):
#             return self.__nombre
#         else:
#             return "No existe"
        
#     def __setitem__(self, index, valor):
#         if (index == "nombre"):
#             self.__nombre = valor

#     def __iter__(self): #hace que se pueda iterar en una lista
#         for i in self.lista:
#             yield i #Es como un return pero cuando vuele¿ve a iterar conserva la posiciion
    
# aux = personaje("Camila")
# # aux["nombre"] = "Juan"
# # print(aux["nombre"])
# # print(aux.nombre)

# contador = 0
# for elemento in aux: #Esto hace que se llame al iter, itera una vez el for y muestra lo que hay dentro de la lista
#     contador += 1
#     print(elemento)
# print(contador) 

#---  YAPA ---
#Se puede heredar

class Persona():
    def __init__(self, id) -> None:
        self.id = id
    def mostrar(self):
        return self.id

class Personaje(Persona):
    def __init__(self, nombre = "") -> None:
        super().__init__(88)
        self.__nombre = nombre
        self.apellido = ""
        self.lista = ["CAMI", "PEPE"]
    def mostrar(self):
            return float(super().mostrar())


aux = Personaje(Persona)
 

print(aux.mostrar())