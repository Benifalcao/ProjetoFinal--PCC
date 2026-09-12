

from django.contrib import admin
from .models import ObjetoTroca


@admin.register(ObjetoTroca)
class ObjetoTrocaAdmin(admin.ModelAdmin):
    list_display = ["id", "objeto", "troca", "quant", "data_troca"]
    list_filter = ["data_troca"]