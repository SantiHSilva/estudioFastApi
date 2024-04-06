from pydantic import BaseModel
from datetime import datetime

class City(BaseModel):
    city_id : int
    city : str
    country_id : int
    last_update : datetime
