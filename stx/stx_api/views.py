from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from .serializers import BookSerializer


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
        data = {
            "external_id": request.data.get("external id"),
            "title": request.data.get("title"),
            "authors": request.data.get("authors"),
            "published_year": request.data.get("published_year"),
            "acquired": request.data.get("acquired"),
            "thumbnail": request.data.get("thumbnail")
        }
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
