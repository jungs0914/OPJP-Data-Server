# # from django.urls import path, include
# # from rest_framework.routers import DefaultRouter
#
# # from books.controller.books_controller import BooksView
#
# # router = DefaultRouter()
# # router.register(r'books', BooksView)
#
# # urlpatterns = [
# #     path('', include(router.urls)),
# #     path('list/', BooksView.as_view({'get': 'list'}), name='books-list'),
# #     path('register/', BooksView.as_view({'post': 'register'}), name='books-register'),
# #     path('read/<int:pk>', BooksView.as_view({'get': 'readBook'}), name='books-read'),
# # ]
#
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
#
# from books.controller.books_controller import BooksController
#
#
# router = DefaultRouter()
# router.register(
#     r"books", BooksController, basename='books'
# )
#
# urlpatterns = [
#     path('', include(router.urls)),
#     path('request-crawl-book-data',
#          BooksController.as_view({ 'get': 'requestCrawlBookData' }),
#          name='도서 정보 크롤링'),
#     path('request-book-list',
#          BooksController.as_view({ 'get': 'requestBookList' }),
#          name='도서 정보 리스트 획득'),
#     path('request-modify-book-description',
#          BooksController.as_view({ 'get': 'requestModifyBookDescription'}),
#          name='도서 이름 변경'),
# ]