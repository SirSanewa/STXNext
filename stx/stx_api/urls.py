from django.urls import path
from .views import ApiSpec

urlpatterns = [
    path('api_spec/', ApiSpec.as_view())
]
