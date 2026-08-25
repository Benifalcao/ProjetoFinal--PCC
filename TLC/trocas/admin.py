
# Register your models here.
from django.contrib import admin

from .models import Usuario, Objeto, Troca

admin.site.register(Usuario)
admin.site.register(Objeto)
admin.site.register(Troca)
