from fastapi import APIRouter
from services.Country import CountryService
from schematics.Country import Country

country_router = APIRouter()
country_service = CountryService()

@country_router.get("/country", responses={200: {"model": Country}})
async def get_countries():
    return country_service.get_all()

@country_router.get("/country/{country_id}", responses={200: {"model": Country}})
async def get_country(country_id: int):
    return country_service.get_model_by_id(country_id)

@country_router.post("/country", responses={200: {"model": Country}})
async def create_country(country: Country):
    return country_service.create(country)

@country_router.put("/country/{country_id}", responses={200: {"model": Country}})
async def update_country(country_id: int, country: Country):
    return country_service.update(country_id, country)

@country_router.delete("/country/{country_id}", responses={200: {"model": Country}})
async def delete_country(country_id: int):
    return country_service.delete(country_id)