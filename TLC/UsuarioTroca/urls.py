from django.urls import path
from . import views

app_name = "UsuarioTroca"
urlpatterns = [
    path("", views.listar_usuarios_troca, name="listar_usuarios_troca"),
    path("criar/", views.criar_usuario_troca, name="criar_usuario_troca"),
]