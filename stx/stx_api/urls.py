from django.urls import path
from .views import ApiSpec, Books, ImportBooks

urlpatterns = [
    path('api_spec', ApiSpec.as_view()),
    path('books', Books.as_view()),
    path('books/<int:book_id>', Books.as_view()),
    path('import', ImportBooks.as_view())
]
