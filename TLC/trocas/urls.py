from django.urls import path
from . import views

app_name = "trocas"

urlpatterns = [
    path("", views.index, name="index"),
    path("listar/", views.listar_trocas, name="listar_trocas"),
    path("criar/", views.criar_troca, name="criar_troca"),
    path("<int:pk>/", views.detalhar_troca, name="detalhar_troca"),      # <--- Detalhar
    path("<int:pk>/editar/", views.editar_troca, name="editar_troca"),  # <--- Editar
    path("<int:pk>/deletar/", views.deletar_troca, name="deletar_troca"),# <--- Deletar
]