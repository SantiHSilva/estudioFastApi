from pydantic import BaseModel

class Country(BaseModel):
    country_id : int
    country : str
    last_update : int
