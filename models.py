from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from typing import List, Optional


from database import Base


class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    age = Column(Integer)
    breed = Column(String(50), index=True)


# Pydantic models
class PetBase(BaseModel):
    name: str
    age: int
    breed: str


class PetCreate(BaseModel):
    name: str
    age: int
    breed: str


class PetUpdate(BaseModel):
    name: str = None
    age: int = None
    breed: str = None


class PetInDBBase(PetBase):
    id: int

    class Config:
        orm_mode = True


class PetInDB(PetBase):
    id: int

    class Config:
        orm_mode = True


class PetDetail(PetInDB):
    pass


class PetList(BaseModel):
    pets: List[PetInDB]
    total: Optional[int] = 0

