from enum import Enum
from pydantic import BaseModel, field_validator, validator
from datetime import date, datetime

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

class Albums(BaseModel):
    title: str
    release_date: date
        
class BandBase(BaseModel):
    name: str
    genre: GenreChoices
    albums: list[Albums] = []
    
class BandCreate(BandBase):
    @field_validator('genre', mode="before")
    def title_case_genre(cls, value):
        return value.title()

class BandWithID(BandBase):
    id: int
    
    

