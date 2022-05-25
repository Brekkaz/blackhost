from database import Database


def seeders():
    try:
        conexion = Database().getDb()
        cur = conexion.cursor()
        cur.execute(
            """INSERT INTO Persons (first_name, last_name, age)
              VALUES ('value1', 'value2', 3);"""
        )
        conexion.commit()
        conexion.close()
    except Exception as e:
        print("Error insertando la informacion: ", e)


seeders()
