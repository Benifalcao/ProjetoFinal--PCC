
# Register your models here.
from django.contrib import admin
from .models import Usuario, Objeto, Troca, UsuarioTroca, ObjetoTroca

admin.site.register(Usuario)
admin.site.register(Objeto)
admin.site.register(Troca)
admin.site.register(UsuarioTroca)
admin.site.register(ObjetoTroca)
