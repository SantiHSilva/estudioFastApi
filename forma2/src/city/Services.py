from forma2.src.city.Model import City
from forma2.src.utils.CRUD import CRUD

class CityService(CRUD):
    def __init__(self):        
        super().__init__(City)
