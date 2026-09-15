from django.urls import path
from . import views

app_name = "ObjetoTroca"
urlpatterns = [
    path("", views.listar_objetos_troca, name="listar_objetos_troca"),
    path("criar/", views.criar_objeto_troca, name="criar_objeto_troca"),
]