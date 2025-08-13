from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, validator
from typing import List

app = FastAPI()

# MODELE

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

class AnimalOut(Animal):
    id: int

# DANE W PAMIĘCI

animals = [
    {"id": 1, "name": "Burek", "species": "dog", "age": 5},
    {"id": 2, "name": "Mruczek", "species": "cat", "age": 3},
    {"id": 3, "name": "Mara", "species": "rat", "age": 1},
    {"id": 4, "name": "Kocik", "species": "cat", "age": 7},
    {"id": 5, "name": "Lala", "species": "spider", "age": 4}
]

# ENDPOINTY

@app.get("/ping")
def ping():
    return {"message": "API is working"}

@app.get("/animals", response_model=List[AnimalOut])
def get_all_animals():
    return animals

@app.get("/animals/{animal_id}", response_model=AnimalOut)
def get_animal(animal_id: int):
    for animal in animals:
        if animal["id"] == animal_id:
            return animal
    raise HTTPException(status_code=404, detail="Animal not found")

@app.post("/animals", response_model=AnimalOut)
def create_animal(animal: Animal):
    new_id = animals[-1]["id"] + 1 if animals else 1
    new_animal = {
        "id": new_id,
        "name": animal.name,
        "species": animal.species,
        "age": animal.age,
    }
    animals.append(new_animal)
    return new_animal

@app.delete("/animals/{animal_id}", response_model=AnimalOut)
def delete_animal(animal_id: int):
    for animal in animals:
        if animal["id"] == animal_id:
            animals.remove(animal)
            return animal
    raise HTTPException(status_code=404, detail="Animal not found")

@app.put("/animals/{animal_id}", response_model=AnimalOut)
def update_animal(animal_id: int, animal_update: AnimalNameUpdate):
    for animal in animals:
        if animal["id"] == animal_id:
            animal["name"] = animal_update.name
            return animal
    raise HTTPException(status_code=404, detail="Animal not found")

@app.get("/animals/search", response_model=List[AnimalOut])
def search_animals(name: str = Query(..., min_length=2)):
    result = [a for a in animals if name.lower() in a["name"].lower()]
    return result
