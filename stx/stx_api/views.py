from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from .serializers import BookReadSerializer, BookWriteSerializer
from .models import Book
from .filter import BookFilter

API_VERSION_DATE = "2022.05.16"


def clear_query_dict(query_dict):
    """
    Strips values of "" in author's list.
    :param query_dict:
    :return: query_dict:
    """
    query_dict_copy = query_dict.copy()
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
