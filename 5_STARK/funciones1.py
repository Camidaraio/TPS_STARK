from data_stark import lista_personajes

def mostrar_lista_personajes():

    for superheroe in lista_personajes:
        print("-------------------------")
        for atributo in superheroe:
            print(atributo, ":", superheroe[atributo])

    return lista_personajes

