  
from models.Country import Country
from services.Utils.CRUD import CRUD

class CountryService(CRUD):
    
    def __init__(self):        
        super().__init__(Country)