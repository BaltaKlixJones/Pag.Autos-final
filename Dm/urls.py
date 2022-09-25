from django.urls import path
from .views import (
        mensajes_privados
)


urlpatterns= [
    
    path("dm/<str:username>", mensajes_privados)
]