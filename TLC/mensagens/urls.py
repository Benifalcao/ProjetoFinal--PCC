from django.urls import path
from . import views

app_name = "mensagens"

urlpatterns = [
    path("", views.minhas_conversas, name="minhas_conversas"),
    path("troca/<int:troca_id>/", views.conversa, name="conversa"),
]