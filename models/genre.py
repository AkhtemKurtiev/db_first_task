from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.database import BaseModel


class Genre(BaseModel):
    __tablename__ = 'genre'

    genre_id = Column(Integer, primary_key=True)
    name_genre = Column(String)

    books = relationship('book', back_populates='genre')
