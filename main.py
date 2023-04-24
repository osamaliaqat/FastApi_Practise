from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import Base, engine, SessionLocal
from models import Pet, PetCreate, PetUpdate, PetInDB, PetList

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# Create a new pet
@app.post("/pets/", response_model=PetInDB)
def create_pet_api(pet: PetCreate, db: Session = Depends(get_db)):
    db_pet = Pet(name=pet.name, age=pet.age, breed=pet.breed)
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet


# Read a pet by ID
@app.get("/pets/{pet_id}", response_model=PetInDB)
def read_pet_api(pet_id: int, db: Session = Depends(get_db)):
    db_pet = db.query(Pet).filter(Pet.id == pet_id).first()
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return db_pet


# Update a pet by ID
@app.put("/pets/{pet_id}", response_model=PetInDB)
def update_pet_api(pet_id: int, pet: PetUpdate, db: Session = Depends(get_db)):
    db_pet = db.query(Pet).filter(Pet.id == pet_id).first()
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    update_data = pet.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_pet, key, value)
    db.commit()
    db.refresh(db_pet)
    return db_pet


# Delete a pet by ID
@app.delete("/pets/{pet_id}")
def delete_pet_api(pet_id: int, db: Session = Depends(get_db)):
    db_pet = db.query(Pet).filter(Pet.id == pet_id).first()
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    db.delete(db_pet)
    db.commit()
    return {"message": "Pet deleted successfully"}


# List all pets
@app.get("/pets/", response_model=PetList)
def list_pets_api(db: Session = Depends(get_db)):
    pets = db.query(Pet).all()
    return PetList(pets=pets)


@app.get("/pets/{pet_id}", response_model=PetInDB)
def list_pets_api(db: Session = Depends(get_db)):
    pets = db.query(Pet).all()
    return PetList(pets=pets)