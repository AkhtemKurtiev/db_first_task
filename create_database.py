from models.author import Author
from models.book import Book
from models.buy_book import Buy_book
from models.buy_step import Buy_step
from models.buy import Buy
from models.city import City
from models.client import Client
from models.database import create_db
from models.genre import Genre
from models.step import Step


def create_database():
    create_db()
    print('Create tables')


if __name__ == '__main__':
    create_database()
