import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Camila
Daraio

En el parque de diversiones "Aventuras Extremas", un grupo de amigos ha decidido disfrutar
del día probando las diferentes atracciones y luego se reúnen en un restaurante para compartir
un delicioso almuerzo. Antes de que llegue la cuenta, deciden crear un programa para calcular
y dividir los gastos de manera equitativa. Se pide ingresar los siguientes datos hasta que el
usuario lo desee:

Para cada amigo:
- Nombre del amigo,
- Plato principal elegido ("Pizza", "Hamburguesa", "Ensalada").
- Cantidad de platos principales pedidos (debe ser al menos 1).
- Bebida elegida ("Refresco", "Agua", "Jugo").
- Cantidad de bebidas pedidas (debe ser al menos 1).

Se conocen los siguientes precios base:
El precio unitario de cada plato principal es de $800.
El precio unitario de cada bebida es de $200.

Una vez ingresados todos los datos, el programa debe calcular e informar lo siguiente:}
A) El total gastado por el grupo (resultante del costo de los platos principales y las
bebidas), y la propina sugerida para el personal del restaurante (esta corresponde al
10% del total gastado).
B) Promedio del dinero gastado en “Jugo”, sobre el grupo de amigos en general.
C) Los porcentajes de cada tipo de platos pedidos (teniendo en cuenta su cantidad).
Ejemplo: [30% pizza, 40% ensaladas, 30% hamburguesas]
D) Además, desean premiar al amigo que realizó la mayor CANTIDAD de pedidos en total
(platos principales + bebidas) con una entrada gratuita para otra atracción del parque
"Aventuras Extremas".




E) REALIZAR DOS PUNTO; EL PRIMERO CORRESPONDIENTE AL ÚLTIMO NÚMERO
DE SU DNI PERSONAL (Ejemplo 4) Y EL SEGUNDO RESTANDO A 9 EL ÚLTIMO

NÚMERO DE SU DNI (Ejemplo 9 - 4 = 5):
0.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan elegido platos
principales del tipo "Pizza" y mostrar la lista completa por print.

1.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan elegido
platos principales del tipo "Hamburguesa" y mostrar la lista completa por print.

2.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan elegido platos
principales del tipo "Ensalada" y mostrar la lista completa por print.

3.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan pedido bebidas
del tipo "Refresco" y mostrar la lista completa por print.

4.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan pedido bebidas
del tipo "Agua" y mostrar la lista completa por print.

5.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado más
de 3 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.

6.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado más
de 5 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.

7.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado más
de 7 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.

8.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado menos
de 3 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.

9.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado menos
de 5 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar2 = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click2)
        self.btn_mostrar2.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.lista_de_nombres = ["Juan", "María", "Pedro", "Laura", "Carlos","Ana", "Luis", "Elena", "Miguel", "Sofía"]

        self.lista_plato_principal = ["Pizza", "Hamburguesa", "Ensalada", "Pizza","Hamburguesa", "Ensalada", "Pizza", "Hamburguesa", "Ensalada", "Pizza"]

        self.lista_cantidad_de_platos = [2, 1, 3, 2, 2, 4, 3, 1, 1, 3]

        self.lista_bebidas_elegidas = ["Refresco", "Agua", "Jugo", "Refresco","Agua", "Jugo", "Refresco", "Agua", "Jugo", "Refresco"]

        self.lista_cantidad_de_bebidas = [2, 1, 5, 3, 2, 5, 1, 2, 1, 3]

        self.lista_hamburguesa = ["María", "Carlos", "Elena"]

        self.lista_pizza = ["Juan", "Laura", "Luis", "Sofía"]

    def btn_mostrar_on_click2(self):
    #1.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan elegido platos principales del tipo "Hamburguesa" y mostrar la lista completa por print.
    
        for i in self.lista_hamburguesa:
            print(i)

    #0.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan elegido platos principales del tipo "Pizza" y mostrar la lista completa por print.
        for i in self.lista_pizza:
            print(i)

    


    def btn_mostrar_on_click(self):
        Precio_unitario_plato = 800
        Precio_unitario_bebida = 200

        suma_total = 0

        contador_jugo = 0
        acumulador_jugo = 0

        acumulador_plato_principal = 0
        acumulador_bebidas = 0

        contador_pizza = 0
        contador_hamburguesa = 0
        contador_ensalada = 0

        max_pedidos = None
        

        cantidad = len(self.lista_de_nombres)

        for indice in range(cantidad):
            acumulador_plato_principal += self.lista_cantidad_de_platos[indice]
            acumulador_bebidas += self.lista_cantidad_de_bebidas[indice]

            cantidad_platos_principal = Precio_unitario_plato * acumulador_plato_principal
            cantidad_bebidas = Precio_unitario_bebida * acumulador_bebidas

            suma_total = cantidad_platos_principal + cantidad_bebidas

            propina = suma_total * 0.10

            if self.lista_bebidas_elegidas[indice] == "Jugo":
                contador_jugo += 1
                acumulador_jugo += Precio_unitario_bebida * self.lista_cantidad_de_bebidas[indice] 

            match self.lista_plato_principal[indice]:
                case "Pizza":
                    contador_pizza += 1
                case "Hamburguesa":
                    contador_hamburguesa += 1
                case "Ensalada":
                    contador_ensalada += 1

            total_pedidos = self.lista_cantidad_de_platos[indice] + self.lista_cantidad_de_bebidas[indice]
            if  max_pedidos == None or total_pedidos > max_pedidos:
                max_pedidos = total_pedidos
                amigo_max_pedidos = self.lista_de_nombres[indice]
                    

        porcentaje_pizza = contador_pizza / cantidad * 100
        porcentaje_ensalada = contador_ensalada / cantidad * 100
        porcentaje_hambuerguesa = contador_hamburguesa / cantidad * 100



        promedio_jugo = acumulador_jugo  / contador_jugo


        

        informe = f"""
        A) El total gastado por el grupo (resultante del costo de los platos principales y las
        bebidas): {suma_total}.  y la propina sugerida para el personal del restaurante (esta corresponde al
        10% del total gastado): {propina} 
        B) Promedio del dinero gastado en “Jugo”, sobre el grupo de amigos en general: {promedio_jugo}
        C) Los porcentajes de cada tipo de platos pedidos (teniendo en cuenta su cantidad).

        pizza: {porcentaje_pizza:.2f}%, 
        Ensaladas {porcentaje_ensalada:.2f}%,  
        Hamburguesas {porcentaje_hambuerguesa:.2f}%

        D) Además, desean premiar al amigo que realizó la mayor CANTIDAD de pedidos en total
        (platos principales + bebidas) con una entrada gratuita para otra atracción del parque
        "Aventuras Extremas". La amiga con mayor cantidad de pedidos es: {amigo_max_pedidos}
"""

        print(informe)







        
    def btn_cargar_on_click(self):
        #   Para cada amigo:
        # - Nombre del amigo,
        # - Plato principal elegido ("Pizza", "Hamburguesa", "Ensalada").
        # - Cantidad de platos principales pedidos (debe ser al menos 1).
        # - Bebida elegida ("Refresco", "Agua", "Jugo").
        # - Cantidad de bebidas pedidas (debe ser al menos 1).

        for _ in range(10000):

            Nombre_amigo = prompt("", "Ingrese su nombre")
            while Nombre_amigo == None or not Nombre_amigo.isalpha():
                Nombre_amigo = prompt("Nombre", "Nombre del amigo")
            self.lista_de_nombres .append(Nombre_amigo)
                
            # Plato principal
            plato_principal = prompt("Plato principal", "Ingrese el plato principal pedido")
            while plato_principal != "Pizza" and plato_principal != "Hamburguesa" and plato_principal != "Ensalada":
                plato_principal = prompt("error", "Ingrese el plato principal pedido")
            self.lista_plato_principal.append(plato_principal)

            cantidad_plato_principal = prompt("Cantidad", "Ingrese la cantidad de platos principales pedidos")
            while int(cantidad_plato_principal) < 1:
                cantidad_plato_principal = prompt("Cantidad", "Ingrese la cantidad de platos principales pedidos")
            self.lista_cantidad_de_platos.append(int(cantidad_plato_principal))


            #Bebidas
            bebidas = prompt("Bebida", "Ingrese la bebida pedido")
            while bebidas != "Refresco" and bebidas != "Agua" and bebidas != "Jugo":
                bebidas = prompt("error", "Ingrese el plato principal pedido")
            self.lista_bebidas_elegidas.append(bebidas)

            cantidad_bebidas = prompt("Bebida", "Ingrese la cantidad de bebidas pedidos")
            while int(cantidad_bebidas) < 1:
                cantidad_bebidas = prompt("Cantidad", "Ingrese la cantidad de platos principales pedidos")
            self.lista_cantidad_de_bebidas.append(int(cantidad_bebidas))

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()