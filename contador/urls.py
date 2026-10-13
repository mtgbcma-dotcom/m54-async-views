from django.urls import path

from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("contador/", views.contador_tempo, name="contador_tempo"),
]
