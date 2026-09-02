from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("listar/", views.listar_trocas, name="listar_trocas"),
    path("criar/", views.criar_troca, name="criar_troca"),
    path("objeto-troca/criar/", views.criar_objeto_troca, name="criar_objeto_troca"),
    path("usuario-troca/listar/", views.listar_usuarios_troca, name="listar_usuarios_troca"),
    path("usuario-troca/criar/", views.criar_usuario_troca, name="criar_usuario_troca"),
]
 