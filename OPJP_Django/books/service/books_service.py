# from abc import abstractmethod, ABC


# class BookService(ABC):
#     @abstractmethod
#     def list(self):
#         pass

#     @abstractmethod
#     def createdBook(self, bookName, bookPrice, bookDescription, bookImage):
#         pass
    
#     @abstractmethod
#     def readBook(self, bookId):
#         pass

from abc import ABC, abstractmethod


class BooksService(ABC):

    @abstractmethod
    def crawlBookData(self):
        pass

    @abstractmethod
    def bookList(self):
        pass

    @abstractmethod
    def requestModifyBookDescription(self):
        pass