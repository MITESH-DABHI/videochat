from django.urls import path
from . import views


urlpatterns = [
    path("", views.lobby),
    path("rooms/", views.room),
]
