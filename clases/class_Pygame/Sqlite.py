import sqlite3
# conexion=sqlite3.connect("bd_btf.db")
# ...
# conexion.close()


# # import sqlite3
# # with sqlite3.connect("bd_btf.db") as conexion:

with sqlite3.connect("bd_test}+.db") as conexion:
    try: #Defenimos la setencia
        sentencias = ''' create table personajes 
                        (
                            id integer primary key autoincrement,
                            nombre text,
                            apellido text,
                            anio real


                            
                        )
                    '''
        conexion.execute(sentencias) #Probamos la sentencia establecida
        print("Se creo una table personajes")
    except sqlite3.OperationalError:
        print("La tabla personajes ya existe")

