from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

NOME_GRUPO_COMUM = 'Usuário comum'


def obter_grupo_comum():
    from objetos.models import Objeto
    from trocas.models import Troca
    from UsuarioTroca.models import UsuarioTroca
    from ObjetoTroca.models import ObjetoTroca
    from .models import Usuario

    grupo, _ = Group.objects.get_or_create(name=NOME_GRUPO_COMUM)

    acoes_por_modelo = {
        Usuario: ['view'],
        Objeto: ['view', 'add', 'change', 'delete'],
        Troca: ['view', 'add', 'change', 'delete'],
        UsuarioTroca: ['view', 'add', 'change', 'delete'],
        ObjetoTroca: ['view', 'add', 'change', 'delete'],
    }

    for modelo, acoes in acoes_por_modelo.items():
        tipo = ContentType.objects.get_for_model(modelo)
        codenames = [f'{acao}_{modelo._meta.model_name}' for acao in acoes]
        permissoes = Permission.objects.filter(content_type=tipo, codename__in=codenames)
        grupo.permissions.add(*permissoes)

    return grupo