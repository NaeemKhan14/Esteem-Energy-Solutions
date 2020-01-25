from django.urls import path
from .views import HomePage,EnergyGeneration,RoomPage

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('energy', EnergyGeneration.as_view(), name='energygeneration'),
    path('room', RoomPage.as_view(), name='roompage'),
]