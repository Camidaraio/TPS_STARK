#Ordenamiento por burbujeo

arrai = [25,2,4,14,67,88,64,23,1,0,12,69]
flag_continuar = False  #Inicializada en falso. Si entra en el if e porque está desordenado.

while (flag_continuar == False):    #Hacemos un flag para que lo haga N veces hasta que esté ordenado. Mientras sea falso vuelve a continuar.
    flag_continuar = True           #Si no entra al ultimo if, a la ultima pasada ya vale true y no vuelve a iterar.
    for i in range(len(arrai)- 1):  #Itero por la posición en la que se encuentra máximo menos 1, uno antes del último.
        if(arrai[i] > arrai[i +1]): #Si la lista en la posición iterada es mayor al elemento de la lista del elemento que está a la derecha del iterado. 
            aux = arrai[i]          #Hacer un auxiliar para que no se sobreescriba, guarda al mayor digamos.
            arrai[i] = arrai[i +1]  #Hacer intercambio del elemento iterado por el de la derecha en caso que sea menor.
            arrai[i +1] = aux       #Ahora el elemento que está a la derecha del que estas iterando actualmente va a valer auxiliar, mayor al de la derecha.
            flag_continuar = False  #falso. Si entra en el if e porque está desordenado.

print(arrai)


lista_a_ordenar = [0, 5, 7, 2, 9, 10, 4, 2]

def buscar_minimo(lista_a_ordenar:list)-> int:
    minimo = 0
    for i in range(len(lista_a_ordenar)):
        if(lista_a_ordenar[i] < lista_a_ordenar[minimo]):
            minimo = i

    return minimo
print(buscar_minimo(lista_a_ordenar))

def algoritmo_ordenamiento_uno(lista_a_ordenar:list)-> list:
    lista_recibida = lista_a_ordenar[:] #Copio la lista existente.
    lista_ordenada = []

    while(len(lista_recibida) > 0):
        minimo = buscar_minimo(lista_recibida)
        lista_ordenada.append(lista_recibida.pop(minimo))



    return lista_ordenada
lista_resultado = algoritmo_ordenamiento_uno(lista_a_ordenar)
print(lista_resultado)


def algoritmo_ordenamiento_dos(lista_a_ordenar:list)-> list:
    lista_recibida = lista_a_ordenar[:] #Copio la lista existente.
    flag_swap = True
    limite = 1

    while(flag_swap == True):
        flag_swap = False
        for i in range(len(lista_recibida)-limite):
            if(lista_recibida[i] > lista_recibida[i+1]):
                lista_recibida[i],lista_recibida[i+1] = lista_recibida[i+1],lista_recibida[i]
                flag_swap = True
        limite += 1

    return lista_recibida

lista_resultado = algoritmo_ordenamiento_dos(lista_a_ordenar)
print(lista_resultado)