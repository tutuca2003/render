from django.urls import path
from . import views

urlpatterns=[
    path('', views.home),
    path('registrarAgente/', views.registrarAgente),
    path('edicionAgente/<legajo>', views.edicionAgente),
    path('editarAgente/', views.editarAgente),
    path('eliminarAgente/<legajo>', views.eliminarAgente),
    path('compensatorios/<legajo>', views.compensatorio),
    path('vacaciones/<legajo>', views.vacaciones),
    path('mecanica/<area>', views.mecanica),
    path('obraCivil', views.obraCivil),
    path('electricidad', views.electricidad),
    path('otrasPlantas', views.otrasPlantas),
    path('articulos/<legajo>', views.articulos),
    path('articulosPantalla/<ide>', views.articulosPantalla),
    path('compensatoriosTotal', views.compensatorioTotal),
    path('articulosTotal', views.articuloTotal),
    path('articulosNitro', views.articuloNitro),
    path('vacacionesTotal', views.vacacioneTotal),
]