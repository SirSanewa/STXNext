from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status


class ApiSpec(APIView):
    def get(self, request):
        return Response(
            {
                "info": {
                    "version": "2022.05.16"
                }
            },
            status=status.HTTP_200_OK)
