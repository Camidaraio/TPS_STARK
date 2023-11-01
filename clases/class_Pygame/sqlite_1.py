import sqlite3

with sqlite3.connect("./class_pygame/bd_btf.db2") as conexion:
    try:
        sentencia = ''' create table personajes
        (
        id integer primary key autoincrement,
        nombre text,
        apellido text,
        anio real
        )
        '''
        conexion.execute(sentencia)
        print("Se creo la tabla personajes")
    except sqlite3.OperationalError:
        print("La tabla personajes ya existe")