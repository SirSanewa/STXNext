from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from .serializers import BookReadSerializer, BookWriteSerializer
from .models import Book, Author

API_VERSION_DATE = "2022.05.16"


class ApiSpec(APIView):
    def get(self, request):
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
        if request.query_params:
            # author podaje w query_param jako str("Autor") wiec trzeba sie pozbyc cudzysłowi
            author = request.query_params.get("author")
            stripped_author = author.strip('"')
            author_details = Author.objects.filter(fullname=stripped_author)
            # te autor_id wyglada okropnie ale nie moge jakos wyciagnac z queryset id
            author_id = author_details.values()[0]["id"]

            # tu chyba może być
            date_from = int(request.query_params.get("from"))
            date_to = int(request.query_params.get("to"))

            # to jest mega łopatologiczne ale nie wiem jak elegancko zamienić "false" na False
            acquired = request.query_params.get("acquired")
            if acquired == "false":
                bool_acquired = False
            elif acquired == "true":
                bool_acquired = True
            else:
                raise ValidationError("Parameter 'acquired' can be only false or true")

            # filtrowanie działa zgodnie z założeniem, i wypluwa wszystko co pasuje, wiec tu ok
            queryset = Book.objects.filter(acquired=bool_acquired) \
                .filter(published_year__gte=date_from, published_year__lte=date_to)\
                .filter(authors__in=[author_id])
            serializer = BookReadSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if book_id:
            book = Book.objects.get(id=book_id)
            serializer = BookReadSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            books = Book.objects.all()
            serializer = BookReadSerializer(books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
