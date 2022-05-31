from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from .serializers import BookReadSerializer, BookWriteSerializer
from .models import Book
from .filter import BookFilter
import requests

API_VERSION_DATE = "2022.05.16"


def clear_query_dict(query_dict):
    """
    Strips values of "" in author's list.
    :param query_dict:
    :return: query_dict:
    """
    query_dict_copy = query_dict.copy()
    query_dict_copy["from_date"] = query_dict_copy.pop("from").pop()
    query_dict_copy["to_date"] = query_dict_copy.pop("to").pop()
    query_dict_copy["author"] = query_dict_copy["author"].strip('"')
    return query_dict_copy


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
        if request.GET:
            cleared_query_dict = clear_query_dict(request.GET)
            f = BookFilter(cleared_query_dict, queryset=Book.objects.all())
            serializer = BookReadSerializer(f.qs.distinct(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if book_id:
            try:
                book = Book.objects.get(id=book_id)
            except ObjectDoesNotExist:
                raise Http404
            serializer = BookReadSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            books = Book.objects.all()
            serializer = BookReadSerializer(books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, book_id=None):
        if book_id:
            book = get_object_or_404(Book.objects.all(), id=book_id)
            book.delete()
            return Response(
                {
                    "result": f"Book id:{book_id} removed"
                },
                status=status.HTTP_202_ACCEPTED)
        return Response(
            {
                "No book id provided"
            },
            status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, book_id=None):
        try:
            book = Book.objects.get(id=book_id)
        except ObjectDoesNotExist:
            raise Http404
        serializer_write = BookWriteSerializer(book, data=request.data, partial=True)
        if serializer_write.is_valid():
            serializer_write.save()
            serializer_read = BookReadSerializer(book)
            return Response(serializer_read.data, status=status.HTTP_200_OK)
        return Response(serializer_write.errors, status=status.HTTP_400_BAD_REQUEST)


class ImportBooks(APIView):
    def post(self, request):
        author_name = self.request.data["author"]
        api_response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={author_name}")
        import_amount = len(api_response.json()["items"])

        for book in api_response.json()["items"]:
            data = {
                "external_id": book["id"],
                "title": book["volumeInfo"]["title"],
                "authors": book["volumeInfo"].get("authors", []),
                # dokończyc co, co jeśli nie ma daty, model zmieniony na akceptacje Null, zmienic kod
                "published_year": book["volumeInfo"]["publishedDate"].split("-")[0],
                "acquired": False,
                "thumbnail": book["volumeInfo"]["infoLink"]
            }
            print(data)
            # serializer = BookWriteSerializer(data=data)
            # if serializer.is_valid():
            #     serializer.save()
