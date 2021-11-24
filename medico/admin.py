from django.contrib import admin

from medico.models import Especialidade, Medico

class detMedico(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'formacao')
    list_filter = ('nome', 'email', 'telefone', 'formacao')
    search_fields = ('nome', 'email', 'formacao')
    # ordering = ('nome', 'email', 'telefone', 'especialidade')

class detEspecialidade(admin.ModelAdmin):
    list_display = ('nome',)
    list_filter = ('nome',)
    search_fields = ('nome',)

admin.site.register(Medico, detMedico)
admin.site.register(Especialidade, detEspecialidade)
