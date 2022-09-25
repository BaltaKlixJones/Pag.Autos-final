from http.client import HTTPResponse
from venv import create
from django.shortcuts import render
from .models import CanalMensaje, Canal, CanalUsuario
from django.http import HttpResponse
# Create your views here.

def mensajes_privados(request, username, *args, **kwargs):
    if not request.user.is_authenticated:
        return HttpResponse("Prohibido")

    mi_username= request.user.username

    canal = Canal.objects.filtrar_ms_por_privado(mi_username, username)
    
    if canal.exists():
        canal_obj= canal.first()
        Usuarios_Canal= canal_obj.canalusuario_set.all().values("usuario__username")
        print(Usuarios_Canal)
        mensaje_canal = canal_obj.canalmensaje_set.all()
        print(mensaje_canal.values("texto"))

    return HttpResponse(f"Nuestro Canal - {canal.count()}")