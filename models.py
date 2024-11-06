from enum import Enum
from pydantic import BaseModel, field_validator
from datetime import date
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

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

class AlbumsBase(SQLModel):
    title: str
    release_date: date
    band_id: int | None = Field(default=None, foreign_key="band.id")
    
class Album(AlbumsBase, table=True):
    id: int = Field(default=None, primary_key=True)
    band: "Band" = Relationship(back_populates="albums")
        
class BandBase(SQLModel):
    name: str
    genre: GenreChoices
    
class BandCreate(BandBase):
    albums: list[AlbumsBase] | None = None
    
    @field_validator('genre', mode="before")
    def title_case_genre(cls, value):
        return value.title()

class Band(BandBase, table=True):
    id: int = Field(default=None, primary_key=True)
    albums: list[Album] = Relationship(back_populates="band")
    
    

