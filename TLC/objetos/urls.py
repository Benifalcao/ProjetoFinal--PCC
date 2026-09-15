from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_objetos, name='listar_objetos'),
    path('criar/', views.criar_objeto, name='criar_objeto'),
    path('<int:pk>/', views.detalhar_objeto, name='detalhar_objeto'),
    path('<int:pk>/editar/', views.editar_objeto, name='editar_objeto'),
    path('<int:pk>/deletar/', views.deletar_objeto, name='deletar_objeto'),
]