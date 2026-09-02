from django.contrib import admin
from .models import Troca, UsuarioTroca, ObjetoTroca

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

# 3. Admins individuais das tabelas intermediárias
@admin.register(UsuarioTroca)
class UsuarioTrocaAdmin(admin.ModelAdmin):
    list_display = ["id", "usuario", "troca", "status", "data_inicio"]
    list_filter = ["status"]

@admin.register(ObjetoTroca)
class ObjetoTrocaAdmin(admin.ModelAdmin):
    list_display = ["id", "objeto", "troca", "quant", "data_troca"]
    list_filter = ["data_troca"]

# 4. Personalização do Painel
admin.site.site_header = "Sistema de Trocas"
admin.site.site_title = "Sistema de Trocas"
admin.site.index_title = "Administração do Sistema de Trocas"