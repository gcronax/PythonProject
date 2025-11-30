import sqlite3
from fastapi import FastAPI

app = FastAPI()

DATABASE = "cars.sqlite"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # devuelve dicts
    return conn


@app.get("/")
def root():
    return {"message": "API Rentify funcionando"}


# ✔ Obtener todos los coches
@app.get("/coches")
def get_coches():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM coches").fetchall()
    conn.close()
    return [dict(row) for row in rows]


# ✔ Obtener coche por ID
@app.get("/coches/{id_coche}")
def get_coche(id_coche: int):
    conn = get_connection()
    row = conn.execute(
        "SELECT * FROM coches WHERE id_coche = ?", (id_coche,)
    ).fetchone()
    conn.close()

    if row is None:
        return {"error": "Coche no encontrado"}

    return dict(row)
