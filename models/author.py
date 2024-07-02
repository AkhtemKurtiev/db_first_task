from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.database import BaseModel


class Author(BaseModel):
    __tablename__ = 'author'

    author_id = Column(Integer, primary_key=True)
    name_author = Column(String)

    books = relationship('book', back_populates='author')
