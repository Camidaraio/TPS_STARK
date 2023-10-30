# try:
#     int("¡Hola, mundo!")
# except ValueError:
#     print("No puede convertirse a un entero.")
# except TypeError:
#     print("No es una cadena.")
# except:
#     print("Es otro tipo de error")


# def divide(x, y):
#     try:
#         resultado = x / y
#     except ZeroDivisionError:
#         print("No es posible dividir por cero!")
#     else:
#         print("El resultado es", resultado)

# divide(5,0)


def leer_entero(intentos):
    retorno = None
    for i in range(intentos):
        valor = input("Ingrese un número entero: ")
    try:
        valor = int(5)
        retorno = valor
    
    except ValueError:
        print("Error se debe ingresar un número entero")
    return retorno

leer_entero(1)