# La división de higiene está trabajando en un control de stock para productos
# sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de
# contagio, de cada una debe obtener los siguientes datos:
# 1. El tipo (validar "barbijo", "jabón" o "alcohol")
# 2. El precio: (validar entre 100 y 300)
# 3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las
# 1000 unidades)
# 4. La marca y el Fabricante.
# Se debe informar lo siguiente:
# A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
# B. Del ítem con más unidades, el fabricante.
# C. Cuántas unidades de jabones hay en total.

tipo = ["barbijo", "jabón", "jabón"]
precio = [100, 120, 125]
cantidad_unidades = [2, 10, 100]
fabricante = ["a", "b", "C"]

barbijo_mas_caro = None
mayor_cant_unidades = None
mayor_fabricante = None

maximo_unidades = None
mayor_fabricante__unidades = None

acumulador_jabon = 0



for i in range(5):
    tipo2 = input("Ingrese el tipo: barbijo, jabón o alcohol: ")
    while tipo2 != "barbijo" and tipo2 != "jabón" and tipo2 != "alcohol":
        tipo2 = input("Ingrese un tipo correcto: barbijo, jabón o alcohol")
    tipo.append(tipo2)

    precio_2 = input("Ingrese el precio entre 100 y 300: ")
    while int(precio_2) > 100 or int(precio_2) < 300 :
        precio_2 = input("Ingrese el precio entre 100 y 300: ")
    precio.append(precio_2)
    print(precio_2)

    cantidad_unidades_2 = input("Ingrese la cantidad de unidades: ")
    while cantidad_unidades_2.isdigit() and int(cantidad_unidades_2) < 1000:
        cantidad_unidades_2 = input("Ingrese la cantidad de unidades: ")
    cantidad_unidades.append(cantidad_unidades_2)
    print(cantidad_unidades_2)

    fabricante_2 = input("Ingrese su fabricante")
    fabricante.append(fabricante_2)

for i in range(len(tipo)):

# A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.

    if barbijo_mas_caro == None or precio[i] > barbijo_mas_caro:
        barbijo_mas_caro = precio[i]
        mayor_cant_unidades = cantidad_unidades[i]
        mayor_fabricante = fabricante[i]

# B. Del ítem con más unidades, el fabricante.

    if maximo_unidades == None or cantidad_unidades[i] > maximo_unidades:
        maximo_unidades = cantidad_unidades[i]
        mayor_fabricante__unidades = fabricante[i]
# C. Cuántas unidades de jabones hay en total.
    if tipo[i] == "jabón":
        acumulador_jabon += cantidad_unidades[i]



informe = f"""
A. Del más caro de los barbijos {barbijo_mas_caro}, la cantidad de unidades {mayor_cant_unidades} y el fabricante {mayor_fabricante}.
B. Del ítem con más unidades {maximo_unidades} el fabricante {mayor_fabricante__unidades}.
C. Cuántas unidades de jabones hay en total. {acumulador_jabon}

"""

print(informe)



