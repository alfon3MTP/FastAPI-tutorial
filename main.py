from fastapi import FastAPI, HTTPException
from schemas import Band, GenreURLChoices

app = FastAPI()
    

BANDS = [
    {'id': 1, 'name': 'The Hives', 'genre': 'Rock'},
    {'id': 2, 'name': 'The Beatles', 'genre': 'Pop'},
    {'id': 3, 'name': 'Amaral', 'genre': 'Acustic'}, 
    {'id': 4, 'name': 'Cafe Quijano', 'genre': 'Blues', 'albums': 
        [{'title': 'La taberna de Buda', 'release_date': '2001-12-14'}]
    },
    {'id': 5, 'name': 'The Police', 'genre': 'Rock'},
]



@app.get('/bands')
async def bands(genre: GenreURLChoices | None) -> list[Band]:
    
    if genre:
        return [
            Band(**b) for b in BANDS if b['genre'].lower() == genre.value
        ]
    
    return [Band(**b) for b in BANDS] 
    
@app.get('/bands/{band_id}')
async def bands(band_id: int) -> Band:
    
    band = next((Band(**b) for b in BANDS if b['id'] == band_id), None)
    
    if band is None:
        raise HTTPException(status_code=404, detail='Band not found')
    
    return band

@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[Band]:
    return [
        Band(**b) for b in BANDS if b['genre'].lower() == genre.value
    ]
    

    
