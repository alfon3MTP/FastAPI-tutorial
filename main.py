from fastapi import FastAPI, HTTPException, Path, Query, Depends
from models import GenreURLChoices, BandCreate, Band, Album
from typing import Annotated
from sqlmodel import Session, select
from contextlib import asynccontextmanager
from db import init_db, get_session

import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    
app = FastAPI(lifespan=lifespan)
    

@app.get('/bands')
async def bands(
    genre: GenreURLChoices | None = None,
    has_albums: bool = False,
    session: Session = Depends(get_session)
) -> list[Band]:
    
    band_list = session.exec(select(Band)).all()

    if genre:
        band_list = [
            b for b in band_list if b.genre.value.lower() == genre.value
        ]

    if has_albums:
        band_list = [b for b in band_list if b.albums]
            
    return band_list 
    


    
@app.get('/bands/{band_id}')
async def band(
    band_id: Annotated[int, Path(title="Tha band ID")],
    session: Session = Depends(get_session)
) -> Band:
    
    band = session.get(Band, band_id)
    
    if band is None:
        raise HTTPException(status_code=404, detail='Band not found')
    
    return band
    
@app.post('/bands')
async def create_band(
    band_data: BandCreate, 
    session: Session = Depends(get_session)
) -> Band:

    band = Band(name=band_data.name, genre=band_data.genre)

    session.add(band)

    if band_data.albums:
        for album in band_data.albums:
            print(band, album)
            album_obj = Album(
                title=album.title, release_date=album.release_date, band=band
            )

            session.add(album_obj)
    
    session.commit()
    session.refresh(band)
        
    return band