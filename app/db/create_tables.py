from database import Database


def create_tables():
    try:
        conexion = Database().getDb()
        cur = conexion.cursor()
        cur.execute(
            """CREATE TABLE Persons (
        id SERIAL,
        first_name varchar(255) NOT NULL,
        last_name varchar(255) NOT NULL,
        age int NOT NULL,
        PRIMARY KEY (id)
      );"""
        )
        conexion.commit()
        conexion.close()
    except Exception as e:
        print("Error creando las tablas: ", e)


create_tables()
