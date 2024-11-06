from enum import Enum
from pydantic import BaseModel, field_validator
from datetime import date
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class GenreURLChoices(Enum):
    ROCK = 'rock'
    POP = 'pop'
    ACUSTIC = 'acustic'
    BLUES = 'blues'
    
class GenreChoices(Enum):
    ROCK = 'Rock'
    POP = 'Pop'
    ACUSTIC = 'Acustic'
    BLUES = 'Blues'

## Base Models
class AlbumBase(SQLModel):
    title: str
    release_date: date
    
class BandBase(SQLModel):
    name: str
    genre: GenreChoices

## Pydantic Check
class BandCreate(BandBase):
    albums: Optional[List[AlbumBase]] = None
    
    @field_validator('genre', mode="before")
    def title_case_genre(cls, value):
        return value.title()

## Model Classes
class Album(AlbumBase, table=True):
    id: int = Field(default=None, primary_key=True)
    band_id: Optional[int] = Field(default=None, foreign_key="band.id")
    band: "Band" = Relationship(back_populates="albums")

class Band(BandBase, table=True):
    id: int = Field(default=None, primary_key=True)
    albums: list[Album] = Relationship(back_populates="band")
    
    

