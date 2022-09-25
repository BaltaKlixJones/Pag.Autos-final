from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    # ..............Pagina de inicio......................
    path("", inicio, name= "inicio"),
    # ...............Vehiculos......................
    path("motos/", motos, name= "motos"),
    path("aviones/", aviones, name= "aviones"),
    path("camiones/", camiones, name= "camiones"),
    path("autos/", autos, name= "autos"),
    path("buscarautos/", buscarautos , name="buscarautos"),
    # ................Autos......................
    path("leerautos/", leerautos, name="leerautos"),
    path("eliminarAuto/<id>", eliminarAuto, name="eliminarAuto"),
    path("editarAuto/<id>", editarAutos, name="editarAuto"),
    # ......................Motos......................
    path("leermotos/", leermotos, name="leermotos"),
    path("eliminarMoto/<id>", eliminarMoto, name="eliminarMoto"),
    path("editarMoto/<id>", editarMotos, name="editarMoto"),
     path("buscarmotos/", buscarmotos , name="buscarmotos"),
   
    # ......................Camiones......................
    path("leercamiones/", leercamiones, name="leercamiones"),
    path("eliminarCamion/<id>", eliminarCamion, name="eliminarCamion"),
    path("editarCamion/<id>", editarCamiones, name="editarCamion"),
     path("buscarcamiones/", buscarcamiones , name="buscarcamiones"),
    # ..............Login, logout, register......................
    path("login/", login_request, name='login'),
    path('register/', register, name= 'register'),
    path('logout/', LogoutView.as_view (template_name= "AppFinal/logout.html"), name= 'logout'),
    # ..................Editar Perfil.......................
    path('editarPerfil/', editarPerfil, name= 'editarPerfil'),
    # ......................Otro......................
    path('agregarAvatar/', agregarAvatar, name= 'agregarAvatar'),
    path('Error/', not_found, name= 'not-found'),
    path('elements/', elem, name='elements'),
    # ......................Otro......................
    


]
