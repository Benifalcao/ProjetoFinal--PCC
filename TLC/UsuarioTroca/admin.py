

from django.contrib import admin
from .models import UsuarioTroca


@admin.register(UsuarioTroca)
class UsuarioTrocaAdmin(admin.ModelAdmin):
    list_display = ["id", "usuario", "troca", "status", "dataInicio"]
    list_filter = ["status"]