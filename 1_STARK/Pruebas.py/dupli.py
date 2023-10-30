from data_stark import lista_personajes

"""
Camila
Daraio

Luego de analizar el set de datos correspondiente resolver el Desafío #01:

A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
fuerza (MÁXIMO)
C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
(MÍNIMO)
D. Recorrer la lista y determinar el peso promedio de los superhéroes
masculinos (PROMEDIO)
E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las
superhéroes de género femenino

NOTA: Se debe construir un menú en el que se sea posible acceder a cada una de
las opciones (A-E)
"""

#A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe

       
        

#B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)
fuerza_max = None
lista_mas_fuertes = []

for heroe in lista_personajes:
    fuerza = int(heroe["fuerza"])
    if fuerza_max == None or fuerza > fuerza_max:
        fuerza_max = fuerza
        lista_mas_fuertes = [heroe]
    elif fuerza == fuerza_max:
        lista_mas_fuertes.append(heroe)




#C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO) 

altura_min  = None
lista_mas_bajos = []

for heroe in lista_personajes:
    altura = float(heroe["altura"])
    if altura_min == None or altura < altura_min:
        altura_min = altura
        lista_mas_bajos = [heroe]
    elif altura == altura_min:
        lista_mas_bajos.append(heroe)



#D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)
contador_m = 0
acumulador_m = 0

for heroe in lista_personajes:
    peso = float(heroe["peso"])
    if heroe["genero"] == "M":
        acumulador_m += peso 
        contador_m += 1 

promedio_peso_m = acumulador_m / contador_m



#E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza 
# promedio de todas las superhéroes de género femenino


contador_f = 0
acumulador_f = 0

for heroe in lista_personajes:
    fuerza = float(heroe["fuerza"])
    if heroe["genero"] == "F":
        acumulador_f+= fuerza 
        contador_f += 1 

promedio_fuerza_f = acumulador_f / contador_f




while(True):
    print("Eliga una opcion: \n",
        "A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe: \n",
        "B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO): \n",
        "C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo(MÍNIMO): \n",
        "D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO): \n",
        "E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas lassuperhéroes de género femenino: \n"
        "F."
        ,)
    print("\n")
    respuesta = input("Ingrese una opcion: ")

    match(respuesta):
        case "A":
            for heroe in lista_personajes:
                print("Nombre:", heroe["nombre"])
                print("Identidad:", heroe["identidad"])
                print("Empresa:", heroe["empresa"])
                print("Altura:", heroe["altura"])
                print("Peso:", heroe["peso"])
                print("Género:", heroe["genero"])
                print("Color de ojos:", heroe["color_ojos"])
                print("Color de pelo:", heroe["color_pelo"])
                print("Fuerza:", heroe["fuerza"])
                print("Inteligencia:", heroe["inteligencia"])
                print("\n")
        case "B":
            if lista_mas_fuertes:
                print("Superheroes mas fuertes:")
                for personajes in lista_mas_fuertes:
                    print("Nombre: ", personajes["nombre"])
                    print("Identidad: ", personajes["identidad"])
                    print("Fuerza: ", personajes["fuerza"])
                    print("Peso: ", personajes["peso"])
                    print("\n")

   
        case "C":
            if lista_mas_bajos:
                print("Superheroes mas bajos:")
                for personajes in lista_mas_bajos:
                    print("Nombre", personajes["nombre"])
                    print("Identidad: ", personajes["identidad"])
                    print("Altura", personajes["altura"])
                    print("\n") 
        case "D":
            print("Peso promedio de los superhéroes masculinos: ", promedio_peso_m)
            print("\n")
        case "E":
            print("superhéroes con fuerza mayor al promedio de F:")
            print(promedio_fuerza_f)
            for heroe in lista_personajes:
                fuerza = float(heroe["fuerza"])
                if fuerza > promedio_fuerza_f: 
                    print("Nombre:", heroe["nombre"])
                    print("Fuerza: ", heroe["fuerza"])
                    print("Peso:", heroe["peso"])
                    print("\n")
        case "F":
            superheroes_por_inteligencia = {}
            for heroe in lista_personajes:
                inteligencia = heroe["inteligencia"]
                if inteligencia not in superheroes_por_inteligencia:
                    superheroes_por_inteligencia[inteligencia] = []
                superheroes_por_inteligencia[inteligencia].append(heroe)

                for inteligencia, valor in superheroes_por_inteligencia.items():
                    print(f"inteligencia: {inteligencia}")
                    print(f"Superhéroes: ")
                    for heroe in valor:
                        print(f"Nombre: {heroe['nombre']}\n") 
                    if inteligencia == "":
                        print(f"Nombre: {heroe['nombre']} no tiene inteligencia \n")
            
        case _:
            break


