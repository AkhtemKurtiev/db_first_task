from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.database import BaseModel


class Buy_book(BaseModel):
    __tablename__ = 'buy_book'

    buy_book_id = Column(Integer, primary_key=True)
    buy_id = Column(Integer, ForeignKey('buy.buy_id'))
    book_id = Column(Integer, ForeignKey('book.book_id'))
    amount = Column(Integer)

    buy = relationship('buy', back_populates='buy_book')
    book = relationship('book', back_populates='buy_books')
