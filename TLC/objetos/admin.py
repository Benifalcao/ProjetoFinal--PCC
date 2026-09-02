from django.contrib import admin
from .models import Objeto


class ObjetoAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "Informações do objeto",
            {
                "fields": [
                    "nome",
                    "descricao",
                    "valor_avaliacao",
                ]
            },
        ),
        (
            "Informações do cadastro",
            {
                "fields": [
                    "usuario",
                    "status",
                ]
            },
        ),
    ]

    list_display = [
        "id",
        "nome",
        "usuario",
        "valor_avaliacao",
        "status",
    ]

    list_filter = [
        "status",
    ]


admin.site.register(Objeto, ObjetoAdmin)