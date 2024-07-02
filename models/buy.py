from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

from models.database import BaseModel


class Buy(BaseModel):
    __tablename__ = 'buy'

    buy_id = Column(Integer, primary_key=True)
    buy_description = Column(Text)
    client_id = Column(Integer, ForeignKey('client.client_id'))

    client = relationship('client', back_populates='buy')
    buy_books = relationship('buy_book', back_populates='buy')
    buy_steps = relationship('buy_step', back_populates='buy')
