from enum import Enum
from pydantic import BaseModel
from datetime import date, datetime

class GenreURLChoices(Enum):
    ROCK = 'rock'
    POP = 'pop'
    ACUSTIC = 'acustic'
    BLUES = 'blues'
    

class Albums(BaseModel):
    title: str
    release_date: date
        
class Band(BaseModel):
    id: int
    name: str
    genre: str
    albums: list[Albums] = []
    