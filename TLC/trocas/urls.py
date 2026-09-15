


from django.urls import path
from . import views

app_name = "trocas"
urlpatterns = [
    path("", views.index, name="index"),
    path("listar/", views.listar_trocas, name="listar_trocas"),
    path("criar/", views.criar_troca, name="criar_troca"),
]