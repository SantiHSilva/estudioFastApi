from fastapi import FastAPI
from forma2.src.city.Routes import city_router
from forma2.src.country.Routes import country_router

app = FastAPI()

app.include_router(city_router)
app.include_router(country_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
