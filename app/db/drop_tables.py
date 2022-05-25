from database import Database


def drop_tables():
    try:
        conexion = Database().getDb()
        cur = conexion.cursor()
        cur.execute("""DROP TABLE IF EXISTS Persons;""")
        conexion.commit()
        conexion.close()
    except Exception as e:
        print("Error eliminando las tablas: ", e)


drop_tables()
