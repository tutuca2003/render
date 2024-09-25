from django.contrib import admin
from .models import Agente,Sector, Area, Compensatorio, Vacaciones, Articulo

class AreaAdmin(admin.ModelAdmin):
    list_filter=('nombre',)

admin.site.register(Agente)
admin.site.register(Sector)
admin.site.register(Area)
admin.site.register(Compensatorio)
admin.site.register(Vacaciones)
admin.site.register(Articulo)




