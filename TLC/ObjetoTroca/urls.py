from django.urls import path
from . import views

app_name = 'objetotroca'

urlpatterns = [
    path('', views.listar_objeto_troca, name='listar'),
    path('criar/', views.criar_objeto_troca, name='criar'),  # <-- Faltava esta linha
    path('detalhar/<int:pk>/', views.detalhar_objeto_troca, name='detalhar'),
    path('editar/<int:pk>/', views.editar_objeto_troca, name='editar'),
    path('deletar/<int:pk>/', views.deletar_objeto_troca, name='deletar'),
]