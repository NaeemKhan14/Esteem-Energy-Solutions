from django.urls import path
from .views import HomePage,EnergyGeneration,RoomPage,Rooms,Plugs

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('energy', EnergyGeneration.as_view(), name='energygeneration'),
    path('room', RoomPage.as_view(), name='roompage'),
    path('room_action', Rooms.as_view(), name='rooms'),
    path('plugs',Plugs.as_view(), name="plugs")
]