from .Model import Country
from forma2.src.utils.CRUD import CRUD

class CountryService(CRUD):
    def __init__(self):        
        super().__init__(Country)