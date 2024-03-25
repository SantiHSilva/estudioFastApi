# coding: utf-8
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime
from config.db import BaseTable

class Country(BaseTable):
    __tablename__ = 'country'

    country_id = Column(Integer, primary_key=True)
    country = Column(String(50), nullable=False)
    last_update = Column(DateTime, nullable=False)

