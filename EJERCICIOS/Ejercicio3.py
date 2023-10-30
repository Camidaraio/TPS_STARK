""" Ejercicio 3:
Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos. 
"""

contador_pares = 0
contador_impares = 0

mayor_par = None
menor_ingresado = None

suma_positivos = 0

producto_negativos = 1


for i in range(5):
    numeros = input("Ingrese 5 numeros")
    numeros_int = int(numeros)
    while numeros_int == 0:
        numeros = input("Ingrese 5 numeros mayor a 0")
    

    if numeros_int % 2 == 0:
        contador_pares += 1
        if mayor_par is None or numeros_int > mayor_par:
            mayor_par = numeros_int
    else:
         contador_impares += 1
        
    if menor_ingresado is None or numeros_int < menor_ingresado:
            menor_ingresado = numeros_int

    if numeros_int > 0:
         suma_positivos += numeros_int
    else:
         producto_negativos *= numeros_int

    

    informe = f"""
    a. Cantidad de pares e impares: {contador_pares} y cantidad de impares: {contador_impares}
    b. El menor número ingresado. {menor_ingresado}
    c. De los pares el mayor número ingresado {mayor_par}.
    d. Suma de los positivos. {suma_positivos}
    e. Producto de los negativos. {producto_negativos}

"""
print(informe )