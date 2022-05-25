from fastapi import FastAPI, HTTPException
from .models.person import Person
from .db.database import Database

app = FastAPI()

conexion = Database().getDb()


@app.get("/persons")
def get_persons():
    try:
        cur = conexion.cursor()
        cur.execute("""SELECT * FROM Persons;""")
        records = cur.fetchall()
        conexion.commit()
    except Exception as e:
        print(e)
        return HTTPException(status_code=500, detail="Error obteniendo la información")

    return HTTPException(status_code=200, detail=records)


@app.get("/persons/{id}")
def get_person_by_id(id: int):
    try:
        conexion = Database().getDb()
        cur = conexion.cursor()
        cur.execute(f"""SELECT * FROM Persons WHERE id={id};""")
        records = cur.fetchone()
        conexion.commit()
    except Exception as e:
        print(e)
        return HTTPException(status_code=500, detail="Error obteniendo la información")

    if records != None:
        return HTTPException(status_code=200, detail=records)
    else:
        return HTTPException(status_code=404, detail="El usuario no existe")


@app.post("/persons")
def create_person(person: Person):
    try:
        conexion = Database().getDb()
        cur = conexion.cursor()
        cur.execute(
            f"""INSERT INTO Persons (first_name, last_name, age)
            VALUES ('{person.first_name}', '{person.last_name}', {person.age});"""
        )
        conexion.commit()
    except Exception as e:
        print(e)
        return HTTPException(status_code=500, detail="Error guardando la información")

    return HTTPException(status_code=200, detail="success")


@app.put("/persons/{id}")
def update_person(id: int, person: Person):
    try:
        conexion = Database().getDb()
        cur = conexion.cursor()
        cur.execute(
            f"""UPDATE Persons
            SET first_name='{person.first_name}', last_name='{person.last_name}', age={person.age}
            WHERE id={id}"""
        )
        conexion.commit()
    except Exception as e:
        print(e)
        return HTTPException(
            status_code=500, detail="Error actualizando la información"
        )

    return HTTPException(status_code=200, detail="success")


@app.delete("/persons/{id}")
def delete_person(id: int):
    try:
        conexion = Database().getDb()
        cur = conexion.cursor()
        cur.execute(f"""DELETE FROM Persons WHERE id={id}""")
        conexion.commit()
    except Exception as e:
        print(e)
        return HTTPException(status_code=500, detail="Error eliminando la información")

    return HTTPException(status_code=200, detail="success")
