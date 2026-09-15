


from django.contrib import admin
from .models import Troca
from UsuarioTroca.models import UsuarioTroca
from ObjetoTroca.models import ObjetoTroca


# 1. Configurações Inlines
class UsuarioTrocaInline(admin.TabularInline):
    model = UsuarioTroca
    extra = 1

class ObjetoTrocaInline(admin.TabularInline):
    model = ObjetoTroca
    extra = 1

# 2. Admin do Model Troca
@admin.register(Troca)
class TrocaAdmin(admin.ModelAdmin):
    list_display = ["id", "status", "data_inicial", "data_resposta", "interessado"]
    list_filter = ["status", "data_inicial", "data_resposta"]
    search_fields = ["status", "interessado"]
    inlines = [UsuarioTrocaInline, ObjetoTrocaInline]

# 3. Personalização do Painel
admin.site.site_header = "Sistema de Trocas"
admin.site.site_title = "Sistema de Trocas"
admin.site.index_title = "Administração do Sistema de Trocas"