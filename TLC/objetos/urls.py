from django.urls import path
from .views import listar_objetos, criar_objeto

urlpatterns = [
    path('', listar_objetos, name='listar_objetos'),
    path('criar/', criar_objeto, name='criar_objeto'),
]