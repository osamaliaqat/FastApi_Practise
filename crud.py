from sqlalchemy.orm import Session
from models import Pet
from sqlalchemy.orm import Session
from . import models


def create_pet(db: Session, pet: models.PetCreate):
    db_pet = models.Pet(name=pet.name, age=pet.age, breed=pet.breed)
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet


def update_pet(db: Session, pet_id: int, pet: models.PetUpdate):
    db_pet = db.query(models.Pet).filter(models.Pet.id == pet_id)
    if not db_pet.first():
        return None
    db_pet.update(pet.dict(exclude_unset=True))
    db.commit()
    db_pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    return db_pet


def get_pet(db: Session, pet_id: int):
    return db.query(Pet).filter(Pet.id == pet_id).first()


def get_pets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pet).offset(skip).limit(limit).all()


def delete_pet(db: Session, pet_id: int):
    pet = db.query(Pet).filter(Pet.id == pet_id).first()
    db.delete(pet)
    db.commit()
