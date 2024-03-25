from pydantic import BaseModel, PastDate
from datetime import timedelta

class City(BaseModel):
    city_id : int
    city : str
    country_id : int
    last_update : PastDate

    class Config:
        orm_mode = True
