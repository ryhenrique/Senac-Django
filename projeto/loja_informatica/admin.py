from django.contrib import admin
from .models import Produto
from .models import Usuario
@admin.register(Usuario)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'ativo')
    list_editable = ('email', 'ativo')
    readonly_fields = ('senha', 'ativo')
    search_fields = ('nome', 'email')
    list_filter = ('ativo',)

admin.site.register(Produto)
