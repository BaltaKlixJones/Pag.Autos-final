from urllib import request
from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView , View
from django.views.defaults import page_not_found

from .forms import AutoFormulario, MotoFormulario, AvionFormulario, CamionFormulario, UserRegisterForm, UserEditForm, AvatarForm
from .models import Autos, Avatar, Motos, Aviones, Camiones

# Create your views here.

# Pagina de inicio
@login_required
def inicio(request):
    return render (request, "AppFinal/inicio.html", {'imagen':obtenerAvatar(request)})

#.............................................................................#
# login
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu= request.POST["username"]
            clave= request.POST["password"]

            usuario = authenticate(username= usu, password= clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppFinal/inicio.html", {'form':form, 'mensaje': f"Bienvenido {usuario}", 'imagen':obtenerAvatar(request)})
            else:
                return render (request, "AppFinal/login.html", {'form':form, 'mensaje': 'Usuario o contraseña incorrectos'})
        else:
            return render (request, "AppFinal/login.html", {'form':form, 'mensaje': 'Usuario o contraseña incorrectos'})
    else:
        form = AuthenticationForm()
        return render (request, "AppFinal/login.html", {'form': form})


# registro

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            
            form.save()
            
            return render (request, "AppFinal/login.html", {'mensaje': f"Usuario creado! Inicia sesion!"})
    else:
        form = UserRegisterForm()
    return render (request, "AppFinal/register.html", {'form': form})




# logout
# fue creado como una vista en funcion de clase


#.............................................................................#

# SECCION AUTOS 
# Pagina para crear y ver autos

@login_required
def autos(request):
    ver_autos= Autos.objects.all()
    if request.method == "POST":
        miFormulario= AutoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            auto=Autos(marca= info['marca'], modelo= info['modelo'], color=info['color'], año= info['año'])
            auto.save()
            return render (request, "AppFinal/autos.html", {"formulario": miFormulario, "mensaje": "Auto creado con exito!" , "ver_autos": ver_autos})
        else:
            return render(request, "AppFinal/autos.html", {"mensaje": "Error!"} )
    else:
        miFormulario= AutoFormulario()

    return render (request, "AppFinal/autos.html", {"formulario": miFormulario,  "ver_autos": ver_autos})

# buscar auto

def buscarautos(request):
    if request.GET["marca"]:
        marca= request.GET["marca"]
        autos_marca= Autos.objects.filter(marca__icontains= marca)
        if len(autos_marca) !=0:
            return render(request, "AppFinal/resultadoBusquedaAutos.html", {"autos": autos_marca})
        else:
            return render(request, "AppFinal/resultadoBusquedaAutos.html", {"mensaje": "No se encontraron resultados"})
    else:
        return render (request, "AppFinal/resultadoBusquedaAutos.html", {"mensaje": "No se enviaron datos!"})

# ver autos para editar
@login_required
def leerautos(request):
    leerautos= Autos.objects.all()
    return render (request, "AppFinal/leerautos.html", {"leerautos": leerautos})


# eliminar autos

def eliminarAuto(request, id ):
    eliminar_auto= Autos.objects.get(id=id)
    eliminar_auto.delete()
    leerautos= Autos.objects.all()
    return render (request, "AppFinal/leerautos.html", {"leerautos": leerautos, "mensaje": "Auto eliminado!"})


# editar autos

def editarAutos(request, id):
    auto = Autos.objects.get(id=id)
    if request.method == "POST":
        form = AutoFormulario(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            auto.marca = info["marca"]
            auto.modelo = info["modelo"]
            auto.color = info["color"]
            auto.año = info["año"]
            auto.save()
            leerautos= Autos.objects.all()
            return render (request, "AppFinal/leerautos.html", {"leerautos": leerautos, "mensaje": "Auto editado!"})

    else:
        formulario = AutoFormulario(initial={"marca": auto.marca , "modelo": auto.modelo , "color": auto.color , "año": auto.año})
        return render (request, "AppFinal/editarAutos.html", {"formulario": formulario, "auto_marca": auto.marca , "id":auto.id})





#.............................................................................#

# SECCION MOTOS 
# Pagina para crear y ver motos

@login_required
def motos(request):
    ver_motos= Motos.objects.all()
    if request.method == "POST":
        miFormulario= AutoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            motos=Motos(marca= info['marca'], modelo= info['modelo'], color=info['color'], año= info['año'])
            motos.save()
            return render (request, "AppFinal/motos.html", {"formulario": miFormulario, "mensaje": "Moto creado con exito!" , "ver_motos": ver_motos})
        else:
            return render(request, "AppFinal/motos.html", {"mensaje": "Error!"} )
    else:
        miFormulario = MotoFormulario()

    return render (request, "AppFinal/motos.html", {"formulario": miFormulario,  "ver_motos": ver_motos})

#buscar moto

def buscarmotos(request):
    if request.GET["marca"]:
        marca= request.GET["marca"]
        motos_marca= Motos.objects.filter(marca__icontains= marca)
        if len(motos_marca) !=0:
            return render(request, "AppFinal/resultadoBusquedaMoto.html", {"motos": motos_marca})
        else:
            return render(request, "AppFinal/resultadoBusquedaMoto.html", {"mensaje": "No se encontraron resultados"})
    else:
        return render (request, "AppFinal/resultadoBusquedaMoto.html", {"mensaje": "No se enviaron datos!"})
# ver motos para editar
@login_required
def leermotos(request):
    leermotos= Motos.objects.all()
    return render (request, "AppFinal/leermotos.html", {"leermotos": leermotos})

# elminar motos

def eliminarMoto(request, id ):
    eliminar_moto= Motos.objects.get(id=id)
    eliminar_moto.delete()
    leermotos= Motos.objects.all()
    return render (request, "AppFinal/leermotos.html", {"leermotos": leermotos, "mensaje": "Moto eliminada!"})
# editar motos


def editarMotos(request, id):
    moto = Motos.objects.get(id=id)
    if request.method == "POST":
        form = MotoFormulario(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            moto.marca = info["marca"]
            moto.modelo = info["modelo"]
            moto.color = info["color"]
            moto.año = info["año"]
            moto.save()
            leermotos= Motos.objects.all()
            return render (request, "AppFinal/leermotos.html", {"leermotos": leermotos, "mensaje": "Moto editada!"})

    else:
        formulario = MotoFormulario(initial={"marca": moto.marca , "modelo": moto.modelo , "color": moto.color , "año": moto.año})
        return render (request, "AppFinal/editarMotos.html", {"formulario": formulario, "motos_marca": moto.marca , "id":moto.id})

#.............................................................................#

# SECCION CAMIONES
# Pagina para crear y ver camiones
@login_required
def camiones(request):
    ver_camiones= Camiones.objects.all()
    if request.method == "POST":
        miFormulario= CamionFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            camion=Camiones(marca= info['marca'], modelo= info['modelo'], color=info['color'], año= info['año'])
            camion.save()
            return render (request, "AppFinal/camiones.html", {"formulario": miFormulario, "mensaje": "Camion creado con exito!" , "ver_camiones": ver_camiones})
        else:
            return render(request, "AppFinal/camiones.html", {"mensaje": "Error!"} )
    else:
        miFormulario= CamionFormulario()

    return render (request, "AppFinal/camiones.html", {"formulario": miFormulario,  "ver_camiones": ver_camiones})

# buscar camion
def buscarcamiones(request):
    if request.GET["marca"]:
        marca= request.GET["marca"]
        camion_marca= Camiones.objects.filter(marca__icontains= marca)
        if len(camion_marca) !=0:
            return render(request, "AppFinal/resultadoBusquedaCamion.html", {"camiones": camion_marca})
        else:
            return render(request, "AppFinal/resultadoBusquedaCamion.html", {"mensaje": "No se encontraron resultados"})
    else:
        return render (request, "AppFinal/resultadoBusquedaCamion.html", {"mensaje": "No se enviaron datos!"})

# ver camiones para editar

def leercamiones(request):
    leercamiones= Camiones.objects.all()
    return render (request, "AppFinal/leercamiones.html", {"leercamiones": leercamiones})

# elminar camiones

def eliminarCamion(request, id ):
    eliminar_camion= Camiones.objects.get(id=id)
    eliminar_camion.delete()
    leercamiones= Camiones.objects.all()
    return render (request, "AppFinal/leercamiones.html", {"leercamiones": leercamiones, "mensaje": "Camion eliminado!"})


# editar camiones

def editarCamiones(request, id):
    camion = Camiones.objects.get(id=id)
    if request.method == "POST":
        form = CamionFormulario(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            camion.marca = info["marca"]
            camion.modelo = info["modelo"]
            camion.color = info["color"]
            camion.año = info["año"]
            camion.save()
            leercamiones= Camiones.objects.all()
            return render (request, "AppFinal/leercamiones.html", {"leercamiones": leercamiones, "mensaje": "Camion editado!"})

    else:
        formulario = CamionFormulario(initial={"marca": camion.marca , "modelo": camion.modelo , "color": camion.color , "año": camion.año})
        return render (request, "AppFinal/editarCamiones.html", {"formulario": formulario, "motos_marca": camion.marca , "id":camion.id})


#.............................................................................#

# SECCION AVIONES
# Pagina para crear y ver aviones
@login_required
def aviones(request):
    if request.method == "POST":
        miFormulario= AvionFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            modelo= info.get("modelo")
            color= info.get("color")
            año= info.get("año")
            avion= Aviones( modelo= modelo, color= color, año= año)
            avion.save()
            return render (request, "AppFinal/aviones.html", {"mensaje": "Avion creado con exito!"})
        else:
            return render(request, "AppFinal/aviones.html", {"mensaje": "Error!"} )
    else:
        miFormulario= AvionFormulario()
        return render (request, "AppFinal/aviones.html", {"formulario": miFormulario})

# Buscar avion 


# ver aviones para editar

# elminar aviones

# editar aviones

#.............................................................................#
# Editar usuario

@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST, instance= usuario)
        if form.is_valid():
            usuario.save()
            return render (request, "AppFinal/inicio.html", { "mensaje": f"Usuario {usuario} editado con exito!"})
    else:
        form = UserEditForm(instance= usuario)
        

        return render (request, "AppFinal/editarPerfil.html", {"form": form, "usuario": usuario, 'imagen':obtenerAvatar(request)})

#............................................................................#
# SECCION AVATAR

# Cambiar avatar
@login_required
def agregarAvatar(request): 
    if request.method == "POST":
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if (len(avatarViejo)> 0):
                avatarViejo.delete()
            avatar=Avatar(user=request.user, imagen= formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, "AppFinal/agregarAvatar.html", {'usuario': request.user, 'mensaje': 'Cambios guardados!'})
    else:
        formulario=AvatarForm()
    return render(request, "AppFinal/agregarAvatar.html", {'form':formulario, 'usuario':request.user, 'imagen':obtenerAvatar(request)})

# Funcion para obtener Avatar

def obtenerAvatar(request):
    lista = Avatar.objects.filter(user=request.user)
    if len(lista) != 0:
        imagen= lista[0].imagen.url
    else: 
        imagen = "/static/AppFinal/assets/images/Avatar-defecto.jpg"
    return imagen


#.............................................................................#
# Nostros

def nosotros(request):
    pass

# Manejo de error 404
def not_found(request):
    return render(request, "AppFinal/not-found.html")





# Creando paginas 



def land(request):
    return render (request, "AppFinal/landing.html")

def gen(request):
    return render (request, "AppFinal/generic.html")

def elem(request):
    return render (request, "AppFinal/elements.html")




#......................................................................................#
#......................................................................................#
#......................................................................................#
#......................................................................................#
#......................................................................................#
#......................................................................................#
#......................................................................................#
#......................................................................................#
#......................................................................................#
#......................................................................................#
#......................................................................................#
#......................................................................................#
#......................................................................................#
#....................MENSAJERIA........................................................#

from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .models import CanalMensaje, CanalUsuario, Canal
from django.http import HttpResponse, Http404, JsonResponse

from .forms import FormMensajes

from django.views.generic.edit import FormMixin

from django.views.generic import View

def leerusuarios(request):
    leerusuarios= request.user
    return render (request, "AppFinal/inbox.html", {"leerusuarioss": leerusuarios})


class Inbox(View):
	def get(self, request):

		inbox = Canal.objects.filter(canalusuario__usuario__in=[request.user.id])


		context = {

			"inbox":inbox
		}

		return render(request, 'AppFinal/inbox.html', context)


class CanalFormMixin(FormMixin):
	form_class =FormMensajes
	#success_url = "./"

	def get_success_url(self):
		return self.request.path

	def post(self, request, *args, **kwargs):

		if not request.user.is_authenticated:
			raise PermissionDenied

		form = self.get_form()
		if form.is_valid():
			canal = self.get_object()
			usuario = self.request.user 
			mensaje = form.cleaned_data.get("mensaje")
			canal_obj = CanalMensaje.objects.create(canal=canal, usuario=usuario, texto=mensaje)
			
			
			return JsonResponse({

					'mensaje':canal_obj.texto,
					'username':canal_obj.usuario.username
					}, status=201)

			

		else:

			

			return super().form_invalid(form)

class CanalDetailView(LoginRequiredMixin, CanalFormMixin, DetailView):
	template_name= 'Dm/canal_detail.html'
	queryset = Canal.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)

		obj = context['object']
		print(obj)

		#if self.request.user not in obj.usuarios.all():
		#	raise PermissionDenied

		context['si_canal_mienbro'] = self.request.user in obj.usuarios.all()

		return context

	#def get_queryset(self):
	#	usuario =self.request.user
	#	username = usuario.username

	#	qs = Canal.objects.all().filtrar_por_username(username)
	#	return qs

class DetailMs(LoginRequiredMixin, CanalFormMixin, DetailView):

	template_name= 'AppFinal/canal_detail.html'

	def get_object(self, *args, **kwargs):

		username = self.kwargs.get("username")
		mi_username = self.request.user.username
		canal, _ = Canal.objects.obtener_o_crear_canal_ms(mi_username, username)

		if username == mi_username:
			mi_canal, _ = Canal.objects.obtener_o_crear_canal_usuario_actual(self.request.user)

			return mi_canal

		if canal == None:
			raise Http404

		return canal

def mensajes_privados(request, username, *args, **kwargs):

	if not request.user.is_authenticated:
		return HttpResponse("Prohibido")

	mi_username = request.user.username

	canal, created = Canal.objects.obtener_o_crear_canal_ms(mi_username, username)

	if created:
		print("Si, fue creado")

	Usuarios_Canal = canal.canalusuario_set.all().values("usuario__username")
	print(Usuarios_Canal)
	mensaje_canal  = canal.canalmensaje_set.all()
	print(mensaje_canal.values("texto"))

	return HttpResponse(f"Nuestro Id del Canal - {canal.id}")


