from fastapi import APIRouter, Response
from forma2.src.city.Services import CityService
from forma2.src.city.Schematics import City

city_router = APIRouter(
    responses={404: {"description": "Not found"}}
)
city_service = CityService()

@city_router.get("/city", responses={200: {"model": City}})
async def get_cities(response : Response):
    datos = city_service.get_all()
    response.status_code = 200 if datos else 204
    return datos

@city_router.get("/city/{city_id}", responses={200: {"model": City}})
async def get_city(city_id: int):
    return city_service.get_model_by_id(city_id)

@city_router.post("/city", responses={200: {"model": City}})
async def create_city(city: City):
    city.last_update.strftime("%Y-%m-%d %H:%M:%S")
    return city_service.create(city)

@city_router.put("/city/{city_id}", responses={200: {"model": City}})
async def update_city(city_id: int, city: City):
    return city_service.update(city_id, city)

@city_router.delete("/city/{city_id}", responses={200: {"model": City}})
async def delete_city(city_id: int):
    return city_service.delete(city_id)
