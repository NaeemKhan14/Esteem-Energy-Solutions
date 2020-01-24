from django.urls import path
from .views import HomePage,RoomPage

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('room', RoomPage.as_view(), name='roompage'),
]