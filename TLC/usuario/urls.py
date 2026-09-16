
from django.urls import path

from . import views

app_name = "usuario"


urlpatterns = [
    path("", views.usuario_list, name="usuario_list"),
    path("<int:usuario_id>/", views.usuario_detail, name="usuario_detail"),
    path("novo/", views.usuario_create, name="usuario_create"),
    path("<int:usuario_id>/editar/", views.usuario_editar, name="usuario_editar"),
    path("<int:usuario_id>/excluir/", views.usuario_excluir, name="usuario_excluir"),
]