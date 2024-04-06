# coding: utf-8
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime
from forma2.src.database import BaseTable

class Country(BaseTable):
    __tablename__ = 'country'

    country_id = Column(Integer, primary_key=True)
    country = Column(String(50), nullable=False)
    last_update = Column(DateTime, nullable=False)

