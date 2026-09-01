
from django.urls import path

from . import views

app_name = "usuario"
urlpatterns = [
    path("", views.usuario_list, name="usuario_list"),
    path("<int:usuario_id>/", views.usuario_detail, name="usuario_detail"),
    path("novo/", views.usuario_create, name="usuario_create"),
]