from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario_view, name='formulario'),
    path('success/', views.success_view, name='success'),
    path('listar/', views.listar_formularios_view, name='listar_formularios'),
]
