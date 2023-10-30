from parte2stark import *
from data_stark import lista_personajes

while(True):
    print("Eliga una opcion: \n",
        "1- Imprimir nombres de NB: \n ",
        "2- superhéroe mas alto del genero F: \n ",
        "3- superhéroe mas alto del genero M: \n ",
        "4- superhéroe mas debil del genero M: \n ",
        "5- superhéroe mas debil del genero NB: \n ",
        "6- fuerza promedio de los superhéroes de género NB: \n ",
        "7- cuántos superhéroes tienen cada tipo de color de ojos: \n,",
        "8- cuántos superhéroes tienen cada tipo de color de pelo: \n",
        "9- todos los superhéroes agrupados por color de ojos: \n",
        "10- todos los superhéroes agrupados por tipo de inteligencia: \n",
        "11- Salir: \n ",
        )
    respuesta = input("Ingrese una opcion: ")

    match(respuesta):
        case "1":
            resultado = mostrar_nombres_NB(lista_personajes)
        case "2":
            resultado = mostrar_superheroe_mas_alto_F(lista_personajes)
            print("Superhéroe más alto del género F:", resultado)

            print("\n")
        case "3":
            resultado = mostrar_superheroe_mas_alto_M(lista_personajes)
            print("Superhéroe más alto del género M:", resultado)

            print("\n")
        case "4":
            resultado = mostrar_superheroe_mas_debil_M(lista_personajes)
            print("Superhéroe más debil del género M:", resultado)
            print("\n")
        case "5":
            resultado = mostrar_superheroe_mas_debil_NB(lista_personajes)
            print("Superhéroe más alto del género NM:", resultado)
            print("\n")
        case "6":
            resultado = mostrar_promedio_fuerza_NB(lista_personajes)
            print("Superhéroe promedio de fuerza del genero M:", resultado)
            print("\n")
        case "7":
            resultado = contar_colores_ojos(lista_personajes)
            print("cuántos superhéroes tienen cada tipo de color de ojos:", resultado)
            print("\n")
        case "8":
            resultado = contar_colores_pelo(lista_personajes)
            print("cuántos superhéroes tienen cada tipo de color de pelo:", resultado)
            print("\n")
        case "9":
            superheroes_por_color_ojos = listar_superheroes_por_color_ojos(lista_personajes)
            for color, superheroes in superheroes_por_color_ojos.items():
                print(f"Color de Ojos: {color}")
                print("Superhéroes:")
                for heroe in superheroes:
                    print(f"Nombre: {heroe['nombre']}\n")  
        
        case "10":
            superheroes_por_inteligencia = listar_superheroes_por_inteligencia(lista_personajes)
            for inteligencia, superheroes in superheroes_por_inteligencia.items():
                print(f"Inteligencia: {inteligencia}\n")
                print(f"Superhéroes: \n")
                for heroe in superheroes:
                    print(f"Nombre: {heroe['nombre']}\n")     
                    if inteligencia == "":
                        print(f"Nombre: {heroe['nombre']} no tiene inteligencia definida \n")  
        
        case _:
            break

