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
"""

#A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe

for  heroe in lista_personajes:
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

       
        

#B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)
fuerza_max = None
superheroes_mas_fuertes = []

for heroe in lista_personajes:
    fuerza_int = float(heroe["fuerza"])
    if fuerza_max is None or fuerza_int > fuerza_max:
        fuerza_max = fuerza_int
        superheroes_mas_fuertes = [heroe]
    elif fuerza_int == fuerza_max:
        superheroes_mas_fuertes.append(heroe)

if superheroes_mas_fuertes:
    print("Superhéroes más fuertes:")
    for superheroe in superheroes_mas_fuertes:
        print("Fuerza:", superheroe["fuerza"])
        print("Identidad:", superheroe["identidad"])
        print("Peso:", superheroe["peso"])
        print("\n")



#C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO) 

altura_mas_baja = None
superheroe_mas_bajo = None

for heroe in lista_personajes:
    altura_int = float(heroe["altura"])
    if altura_mas_baja == None or altura_int < altura_mas_baja:
        altura_mas_baja = altura_int
        superheroe_mas_bajo = heroe

if superheroe_mas_bajo:
    print("Superhéroe más bajo:")
    print("Altura:", superheroe_mas_bajo["altura"])
    print("Nombre:", superheroe_mas_bajo["nombre"])
    print("Identidad:", superheroe_mas_bajo["identidad"])
    print("\n")

#D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)
contador_masculino = 0
acumulador_peso_masculinos = 0

for heroe in lista_personajes:
    if heroe["genero"] == "M":
        peso_int = float(heroe["peso"])
        contador_masculino += 1
        acumulador_peso_masculinos += peso_int

if contador_masculino > 0:        
    promedio_peso_masculinos = acumulador_peso_masculinos / contador_masculino

print("Peso promedio de los superhéroes masculinos: ", promedio_peso_masculinos)
print("\n")


#E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza 
# promedio de todas las superhéroes de género femenino
contador_femenino = 0
acumulador_fuerza_femenino = 0

for heroe in lista_personajes:
    
    if heroe["genero"] == "F":
        fuerza_int = float(heroe["fuerza"])
        contador_femenino += 1
        acumulador_fuerza_femenino += fuerza_int
   

if contador_femenino > 0:
    promedio_peso_femenino = acumulador_fuerza_femenino / contador_femenino
print("superhéroes con fuerza mayor al promedio de F:")
print(promedio_peso_femenino)

for heroe in lista_personajes:
    fuerza_int = float(heroe["fuerza"])
    if fuerza_int > promedio_peso_femenino:
        print("Nombre:", heroe["nombre"])
        print("Fuerza:", superheroe["fuerza"])
        print("Peso:", heroe["peso"])
