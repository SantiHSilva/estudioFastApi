  
from models.City import City
from services.Utils.CRUD import CRUD

class CityService(CRUD):
    
    def __init__(self):        
        super().__init__(City)