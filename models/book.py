from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.database import BaseModel


class Book(BaseModel):
    __tablename__ = 'book'

    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('author.author_id'))
    genre_id = Column(Integer, ForeignKey('genre.genre_id'))
    price = Column(Integer)
    amount = Column(Integer)

    author = relationship('author', back_populates='book')
    genre = relationship('genre', back_populates='book')
    buy_books = relationship('buy_book', back_populates='book')
