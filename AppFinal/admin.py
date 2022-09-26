from django.contrib import admin
from .models import Autos, Aviones, Camiones, Motos, Avatar, Canal, CanalUsuario, CanalMensaje

# Register your models here.

class CanalMensajeInline(admin.TabularInline):
	model = CanalMensaje
	extra = 1

class CanalUsuarioInline(admin.TabularInline):
	model = CanalUsuario
	extra = 1


class CanalAdmin(admin.ModelAdmin):
	inlines = [CanalMensajeInline, CanalUsuarioInline]

	class Meta:
		model = Canal

admin.site.register(Autos)
admin.site.register(Aviones)
admin.site.register(Camiones)
admin.site.register(Motos)
admin.site.register(Avatar)
admin.site.register(Canal, CanalAdmin)
admin.site.register(CanalUsuario)
admin.site.register(CanalMensaje)



