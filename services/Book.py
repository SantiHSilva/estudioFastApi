from models.book import Book
from services.Utils.CRUD import CRUD

class BookService(CRUD):
    
    def __init__(self):        
        super().__init__(Book)
    