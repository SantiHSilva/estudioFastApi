from fastapi import FastAPI
from pydantic import BaseModel
from routes.Country import country_router
from routes.City import city_router

class PruebaSchematic(BaseModel):
    nombre: str
    apellido: str
    edad: int

app = FastAPI()
app.include_router(city_router, tags=["City"], prefix="/city")
app.include_router(country_router, tags=["Country"], prefix="/country")

@app.get("/", response_model=PruebaSchematic)
def read_root():
    return {"Hello": "World"}
