from django.urls import path
from . import views

app_name = 'usuariotroca'

urlpatterns = [
    path('', views.listar_usuario_troca, name='listar'),
    path('criar/', views.criar_usuario_troca, name='criar'),  # <-- Faltava esta linha
    path('detalhar/<int:pk>/', views.detalhar_usuario_troca, name='detalhar'),
    path('editar/<int:pk>/', views.editar_usuario_troca, name='editar'),
    path('deletar/<int:pk>/', views.deletar_usuario_troca, name='deletar'),
]