# from django.shortcuts import render
# from rest_framework import viewsets, status
# from rest_framework.response import Response

# from books.entity.books import Books
# from books.serializers import BookSerizlier
# from books.service.books_service_impl import BookServiceImpl

# # viewsets를 사용하려면 rest_framework가 설정되어야 한다.
# # pip install djangorestframework
# class BooksView(viewsets.ViewSet):
#     queryset = Books.objects.all()
#     booksService = BookServiceImpl.getInstance()

#     def list(self, request):
#         booksList = Books.objects.all()
#         serializer = BookSerizlier(booksList, many=True)
#         return Response(serializer.data)
    
#     def register(self, request):
#         try:
#             data = request.data

#             bookImage = request.FILES.get('bookImage')
#             bookName = data.get('bookName')
#             bookPrice = data.get('bookPrice')
#             bookDescription = data.get('bookDescription')

#             if not all([bookImage, bookName, bookPrice, bookDescription]):
#                 return Response({ 'error': '책을 등록해주세요!'}, status=status.HTTP_400_BAD_REQUEST)
            
#             savedBook = self.booksService.createBook(bookName, bookPrice, bookDescription, bookImage)

#             serializer = BookSerizlier(savedBook)

#             return Response(serializer.data, status=status.HTTP_200_OK)
        
#         except Exception as e:
#             print({ 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
#     def readBook(self, request, pk=None):
#         book = self.booksService.readBook(pk)
#         serilizer = BookSerizlier(book)
#         return Response(serilizer.data)

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status

from books.service.books_service_impl import BooksServiceImpl


class BooksController(viewsets.ViewSet):
    __bookService = BooksServiceImpl.getInstance()

    def requestCrawlBookData(self, request):
        isSuccess = self.__bookService.crawlBookData()
    
        return JsonResponse({'success': isSuccess})
    
    def requestBookList(self, request):
        try:
            bookListDataFrame = self.__bookService.bookList()
            print(
                f"bookListDataFrame: {bookListDataFrame}"
            )

            return JsonResponse(
                bookListDataFrame.to_dict(orient='records'),
                safe=False
            )
        
        except Exception as e:
            return JsonResponse(
                {"error": str(e)},
                status = status.HTTP_400_BAD_REQUEST,
            )
    
    def requestModifyBookDescription(self, request):
        isSuccess = self.__bookService.requestModifyBookDescription()

        if isSuccess:
            return JsonResponse({'success': True})
        else:
            return JsonResponse(
                {'success': False, 'error': 'Failed to modify book description'},
                status = status.HTTP_400_BAD_REQUEST,
            )