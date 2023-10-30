from data_stark import lista_personajes

"""
Camila Daraio

Desafío #02:
Usando como base lo realizado en el anterior desafío realizar los siguientes
informes en un menú
1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género NB
2. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
3. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
4. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
5. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
6. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
género NB
7. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
8. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
9. Listar todos los superhéroes agrupados por color de ojos.
10. Listar todos los superhéroes agrupados por tipo de inteligencia

NOTA: Se debe aplicar el tema Funciones visto en clase para cada opción del menú 

"""
#1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
def mostrar_nombres_NB(lista_personajes):
    """ 
    Recorre la lista imprimiendo por consola el nombre de cada superhéroe de género F
    Recibe lista de nombres
    devuelve: nombres
    """
    superhéroes_NB = []
    for heroe in lista_personajes:
        if heroe["genero"] == "NB":
            superhéroes_NB.append(heroe["nombre"])

    if superhéroes_NB not in lista_personajes:
        print("No existe el genero NB \n")
    else:
        return superhéroes_NB


#2. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
def mostrar_superheroe_mas_alto_F(lista_personajes) -> list[dict] :
    """ 
    Recorre la lista imprimiendo los superhéroe más alto de género F
    Recibe: alturas
    devuelve: nombres
    """
    altura_max_f = None
    superheroe_mas_alto = None    
    for heroe in lista_personajes:
        if heroe["genero"] == "F":
            altura = float(heroe["altura"])
            if altura_max_f == None or altura > altura_max_f:
                altura_max_f = altura
                superheroe_mas_alto = heroe
 


    return superheroe_mas_alto["nombre"]


    # if superheroe_mas_alto:
    #     print("superheroe mas alto F: ")
    #     print("Nombre: ", superheroe_mas_alto["nombre"])
    #     print("Altura: ", superheroe_mas_alto["altura"])


# 3. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
def mostrar_superheroe_mas_alto_M(lista_personajes):
    """ 
    Recorre la lista imprimiendo los superhéroe más alto de género M
    Recibe: alturas
    devuelve: nombres
    """
    altura_max_m = None
    superheroe_mas_alto_m = None    
    for heroe in lista_personajes:
        if heroe["genero"] == "M":
            altura = float(heroe["altura"])
            if altura_max_m == None or altura > altura_max_m:
                altura_max_m = altura
                superheroe_mas_alto_m = heroe
                
    return superheroe_mas_alto_m["nombre"]


#4. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
def mostrar_superheroe_mas_debil_M(lista_personajes):
    """ 
    Recorre la lista imprimiendo los superhéroe más débil de género M
    Recibe: fuerza
    devuelve: nombres
    """
    fuerza_min_m = None
    superheroe_mas_debil_m = None    
    for heroe in lista_personajes:
        if heroe["genero"] == "M":
            fuerza = float(heroe["fuerza"])
            if fuerza_min_m == None or fuerza > fuerza_min_m:
                fuerza_min_m = fuerza
                superheroe_mas_debil_m = heroe
                
    return superheroe_mas_debil_m["nombre"]


#5. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
def mostrar_superheroe_mas_debil_NB(lista_personajes):
    """ 
    Recorre la lista imprimiendo los superhéroe más débil de género NB
    Recibe: fuerza
    devuelve: nombres
    """
    fuerza_min_nm = None
    superheroe_mas_debil_nm = None    
    for heroe in lista_personajes:
        if heroe["genero"] == "NB":
            fuerza = float(heroe["fuerza"])
            if fuerza_min_nm == None or fuerza > fuerza_min_nm:
                fuerza_min_nm = fuerza
                superheroe_mas_debil_nm = heroe

    if superheroe_mas_debil_nm is None:
        print("No existe el genero NB")
    else:
        return superheroe_mas_debil_nm
                
    return superheroe_mas_debil_nm 


#6.Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
def mostrar_promedio_fuerza_NB(lista_heroes):
    """ 
    Recorre la lista imprimiendo la fuerza promedio de los superhéroes del género NB
    Recibe: fuerza
    devuelve: nombres
    """

    suma_fuerza_nb = 0
    contador_fuerza_masculino = 0
    for heroe in lista_heroes:
        if heroe["genero"] == "NB":
            suma_fuerza_nb  += int(heroe["fuerza"])
            contador_fuerza_masculino += 1
    if suma_fuerza_nb != 0:
        promedio_fuerza_nb = suma_fuerza_nb / contador_fuerza_masculino
        mensaje =print(f"La fuerza promedio de los superheroes no binarios es de{promedio_fuerza_nb}")
    else:
        mensaje = print("No hay personajes NB")
    return mensaje


#7. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
def contar_colores_ojos(lista_personajes):
    """ 
    Recorre la lista cuántos superhéroes tienen cada tipo de color de ojos.
    Recibe: color de ojos
    devuelve: colores
    """
    colores = {}
    for heroe in lista_personajes:
        color_ojos = heroe["color_ojos"]
        if color_ojos not in colores:
            colores[color_ojos] = 1
        else:
            colores[color_ojos] += 1
    return colores


# 8. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
def contar_colores_pelo(lista_personajes):
    """ 
    Recorre la lista cuántos superhéroes tienen cada tipo de color de pelo.
    Recibe: color de pelo
    devuelve: colores
    """
    tipo_pelo = {}
    for heroe in lista_personajes:
        color_pelo = heroe["color_pelo"]
        if color_pelo not in tipo_pelo:
            tipo_pelo[color_pelo] = 1
        else:
            tipo_pelo[color_pelo] += 1
    return tipo_pelo


#9. Listar todos los superhéroes agrupados por color de ojos.
def listar_superheroes_por_color_ojos(lista_personajes):
    """
    Recorre la lista y lista todos los superhéroes agrupados por color de ojos.
    Recibe: color de ojos
    Devuelve: Un diccionario donde las claves son los colores de ojos y los valores son listas de superhéroes con ese color de ojos.
    """
    superheroes_por_color_ojos = {}
    for heroe in lista_personajes:
        color_ojos = heroe["color_ojos"]
        if color_ojos not in superheroes_por_color_ojos:
            superheroes_por_color_ojos[color_ojos] = []
        superheroes_por_color_ojos[color_ojos].append(heroe)
        
    return superheroes_por_color_ojos


#10. Listar todos los superhéroes agrupados por tipo de inteligencia
def listar_superheroes_por_inteligencia(lista_personajes):
    """
    Recorre la lista y lista todos los superhéroes agrupados por color de pelo.
    Recibe: color de pelo
    Devuelve: Un diccionario donde las claves son los colores de pelo y los valores son listas de superhéroes con ese color de pelo.
    """
    superheroes_por_inteligencia = {}
    for heroe in lista_personajes:
        inteligencia = heroe["inteligencia"]
        if inteligencia not in superheroes_por_inteligencia:
            superheroes_por_inteligencia[inteligencia] = []
        superheroes_por_inteligencia[inteligencia].append(heroe)

    return superheroes_por_inteligencia


