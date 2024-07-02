from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.database import BaseModel


class Client(BaseModel):
    __tablename__ = 'client'

    client_id = Column(Integer, primary_key=True)
    name_client = Column(String)
    city_id = Column(Integer, ForeignKey('city.city_id'))
    email = Column(String)

    city = relationship('city', back_populates='client')
    buy = relationship('buy', back_populates='client')
