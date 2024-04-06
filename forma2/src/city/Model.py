from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey
from forma2.src.database import BaseTable

class City(BaseTable):
    __tablename__ = 'city'

    city_id = Column(Integer, primary_key=True)
    city = Column(String(50), nullable=False)
    country_id = Column(ForeignKey('country.country_id'), nullable=False, index=True)
    last_update = Column(DateTime(timezone=True), nullable=False)

    country = relationship('Country')
