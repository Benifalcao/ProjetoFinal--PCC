
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from TLCC import views as auth_views


urlpatterns = [
    path('', login_required(TemplateView.as_view(template_name='bem_vindo.html'), login_url='login'), name='bem_vindo'),
    path('login/', auth_views.login_view, name='login'),
    path('logout/', auth_views.logout_view, name='logout'),
    path('trocas/', include('trocas.urls')),
    path('objetos/', include('objetos.urls')),
    path('usuario/', include('usuario.urls')),
    path('usuario-troca/', include('UsuarioTroca.urls')),
    path('objeto-troca/', include('ObjetoTroca.urls')),
    path('mensagens/', include('mensagens.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
