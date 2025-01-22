# # import os
#
# # from OPJP_Django import settings
# # from books.entity.books import Books
# # from books.repository.books_repository import BooksRepository
#
#
# # class BookRepositoryImpl(BooksRepository):
# #     __instance = None
#
# #     def __new__(cls):
# #         if cls.__instance is None:
# #             cls.__instance = super().__new__(cls)
#
# #         return cls.__instance
#
# #     @classmethod
# #     def getInstance(cls):
# #         if cls.__instance is None:
# #             cls.__instance = cls()
#
# #         return cls.__instance
#
# #     def list(self):
# #         return Books.objects.all().order_by('registerDate')
#
# #     def create(self, bookName, bookPrice, bookDescription, bookImage):
# #         uploadDirectory = os.path.join(
# #             settings.BASE_DIR,
# #             # 무엇을 넣어야 할까요?
# #         )
# #         if not os.path.exists(uploadDirectory):
# #             os.makedirs(uploadDirectory)
#
# #         imagePath = os.path.join(uploadDirectory, bookImage.name)
# #         with open(imagePath, 'wb+') as destination:
# #             for chunk in bookImage.chunks():
# #                 destination.write(chunk)
#
# #             destination.flush()
# #             os.fsync(destination.fileno())
#
# #         book = Books(
# #             bookName=bookName,
# #             bookDescription=bookDescription,
# #             bookPrice=bookPrice,
# #             bookImage=bookImage.name
# #         )
# #         book.save()
#
# #         savedBook = Books.objects.get(bookId=book.bookId)
# #         print(f"savedBook: {savedBook.bookImage}")
# #         return savedBook
#
# #     def findByBookId(self, bookId):
# #         try:
# #             return Books.objects.get(bookId=bookId)
# #         except Books.DoesNotExist:
# #             return None
#
# from books.entity.books import Books
# from books.repository.books_repository import BooksRepository
#
# import pandas as pd
#
#
# class BooksRepositoryImpl(BooksRepository):
#     __instance = None
#
#     def __new__(cls):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#
#         return cls.__instance
#
#     @classmethod
#     def getInstance(cls):
#         if cls.__instance is None:
#             cls.__instance = cls()
#
#         return cls.__instance
#
#     def create(self, bookData):
#         book = Books(**bookData)
#         book.save()
#         return book
#
#     def createMany(self, bookDataList):
#         books = []
#         for bookData in bookDataList:
#             book = Books(**bookData)
#             book.save()
#             books.append(book)
#         return books
#
#     def findAll(self)-> pd.DataFrame:
#         books = Books.objects.all().values()
#         return pd.DataFrame(books)
#
#     def save(self, bookData):
#         try:
#             # 데이터베이스에서 ID로 기존 레코드 검색(id)
#             book = Books.objects.get(id=bookData['bookId'])
#
#             # 업데이트할 필드 설정
#             # book.bookName = bookData['bookName']
#             book.bookDescription = bookData['bookDescription']
#
#             # 저장
#             book.save()
#             print(
#                 f"Book with ID {book.bookId} successfully updated."
#             )
#         except Books.DoesNotExist:
#             print(
#                 f"Book with ID {bookData['bookId']} does not exist in the database."
#             )
#         except Exception as e:
#             print(
#                 f"An error occurred while saving the book data: {e}"
#             )