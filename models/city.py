from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from models.database import BaseModel


class City(BaseModel):
    __tablename__ = 'city'

    city_id = Column(Integer, primary_key=True)
    name_city = Column(String)
    days_delivery = Column(Date)

    clients = relationship('client', back_populates='city')
