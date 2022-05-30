from django.urls import path
from .views import ApiSpec, Books

urlpatterns = [
    path('api_spec/', ApiSpec.as_view()),
    path('books/', Books.as_view())
]
