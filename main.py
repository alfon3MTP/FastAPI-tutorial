from fastapi import FastAPI, HTTPException
from schemas import BandBase, BandWithID, BandCreate, GenreURLChoices

app = FastAPI()
    

BANDS = [
    {'id': 1, 'name': 'The Hives', 'genre': 'Rock'},
    {'id': 2, 'name': 'The Beatles', 'genre': 'Pop'},
    {'id': 3, 'name': 'Amaral', 'genre': 'Acustic'}, 
    {'id': 4, 'name': 'Cafe Quijano', 'genre': 'Blues', 'albums': 
        [{'title': 'La taberna de Buda', 'release_date': '2001-12-14'}]
    },
    {'id': 5, 'name': 'The Police', 'genre': 'Rock', 'albums': 
        [{'title': 'Certifiable', 'release_date': '2007-12-11'}]
    },
]



@app.get('/bands')
async def bands(
    genre: GenreURLChoices | None,
    has_albums: bool = False
) -> list[BandWithID]:
    
    band_list = [BandWithID(**b) for b in BANDS]
    
    
    if genre:
        band_list = [
            b for b in band_list if b.genre.value.lower() == genre.value
        ]

    if has_albums:
        band_list = [b for b in band_list if b.albums]
            
    return band_list 
    
@app.get('/bands/{band_id}')
async def bands(band_id: int) -> BandWithID:
    
    band = next((BandWithID(**b) for b in BANDS if b['id'] == band_id), None)
    
    if band is None:
        raise HTTPException(status_code=404, detail='Band not found')
    
    return band

@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    return [
        b for b in BANDS if b['genre'].lower() == genre.value
    ]
    

    
@app.post('/bands')
async def create_gand(band_data: BandCreate) -> BandWithID:
    id = BANDS[-1]['id'] + 1
    band = BandWithID(id=id, **band_data.model_dump()).model_dump()
    BANDS.append(band)

    print(band)

    return band