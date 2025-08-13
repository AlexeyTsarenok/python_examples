import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
from typing import List

app = FastAPI()

DB_NAME = "animals.db"

# 🧬 MODELE

class Animal(BaseModel):
    name: str
    species: str
    age: int

    @validator("name")
    def validate_name(cls, v):
        if len(v.strip()) < 2:
            raise ValueError("Name must be at least 2 characters long")
        return v

class AnimalNameUpdate(BaseModel):
    name: str

    @validator("name")
    def validate_name(cls, v):
        if len(v.strip()) < 2:
            raise ValueError("Name must be at least 2 characters long")
        return v

# 🛠️ INICJALIZACJA BAZY

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS animals (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            species TEXT NOT NULL,
            age INTEGER NOT NULL,
            UNIQUE(name, species)
        );
    """)
    conn.commit()
    conn.close()

init_db()

# 🔧 ENDPOINTY

@app.get("/ping")
def ping():
    return {"message": "API is working"}

@app.get("/animals")
def get_all_animals():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM animals")
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/animals/{animal_id}")
def get_animal(animal_id: int):
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM animals WHERE id = ?", (animal_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return dict(row)
    raise HTTPException(status_code=404, detail="Animal not found")

@app.post("/animals")
def create_animal(animal: Animal):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO animals (name, species, age) VALUES (?, ?, ?)",
            (animal.name, animal.species, animal.age)
        )
        conn.commit()
        new_id = cur.lastrowid
        cur.execute("SELECT * FROM animals WHERE id = ?", (new_id,))
        row = cur.fetchone()
        return dict(row)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="Animal with this name and species already exists")
    finally:
        conn.close()

@app.put("/animals/{animal_id}")
def update_animal(animal_id: int, update: AnimalNameUpdate):
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("UPDATE animals SET name = ? WHERE id = ?", (update.name, animal_id))
    conn.commit()
    cur.execute("SELECT * FROM animals WHERE id = ?", (animal_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return dict(row)
    raise HTTPException(status_code=404, detail="Animal not found")

@app.delete("/animals/{animal_id}")
def delete_animal(animal_id: int):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM animals WHERE id = ?", (animal_id,))
    row = cur.fetchone()
    if not row:
        conn.close()
        raise HTTPException(status_code=404, detail="Animal not found")
    cur.execute("DELETE FROM animals WHERE id = ?", (animal_id,))
    conn.commit()
    conn.close()
    return {"message": "Animal deleted"}
