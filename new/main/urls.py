from django.urls import path
from .views import AboutPageView, HomePageView, PlantDataJsonView


urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('api/v1/plantinfo/', PlantDataJsonView.as_view(), name='plantinfo'),
]