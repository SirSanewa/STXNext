from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from .serializers import BookReadSerializer, BookWriteSerializer
from .models import Book


API_VERSION_DATE = "2022.05.16"


class ApiSpec(APIView):
    def get(self, response):
        return Response(
            {
                "info": {
                    "version": API_VERSION_DATE
                }
            },
            status=status.HTTP_200_OK)


class Books(APIView):
    def post(self, request):
        serializer_write = BookWriteSerializer(data=request.data)

        if serializer_write.is_valid():
            new_book = serializer_write.save()
            serializer_read = BookReadSerializer(new_book)
            return Response(serializer_read.data, status=status.HTTP_201_CREATED)
        return Response(serializer_write.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, book_id=None):
        if book_id:
            book = Book.objects.get(id=book_id)
            serializer = BookReadSerializer(book)
        else:
            books = Book.objects.all()
            serializer = BookReadSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

