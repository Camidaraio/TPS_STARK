


class Alumno:

    def __init__(self,nombre,apellido,edad,materias):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.materias = materias

    '''
    def get_edad(self):
        return self.__edad

    def set_edad(self,edad_nueva):
        self.__edad = edad_nueva
    '''

    
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self,nueva_edad):
        if nueva_edad < 0:
            print("Che una edad no puede ser cero!!!")
        else:
            self.__edad = nueva_edad
    

    def mostrar_nombre(self):
        return f"{self.__nombre}, {self.__apellido}"



    



alumno_uno = Alumno("Marina","Cardozo",22,["Programacion"])

print(alumno_uno)
print(alumno_uno.mostrar_nombre())
print(alumno_uno.materias)

print("Edad!")

#print(alumno_uno.get_edad()) esto seria llamando al metodo
print(alumno_uno.edad) #esto seria llamando a la propiedad

print("modificacion")

alumno_uno.edad = 35
print(alumno_uno.edad)


