from django.contrib import admin

from medico.models import Medico

class detMedico(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'especialidade')
    list_filter = ('nome', 'email', 'telefone', 'especialidade')
    search_fields = ('nome', 'email', 'especialidade')
    # ordering = ('nome', 'email', 'telefone', 'especialidade')

admin.site.register(Medico, detMedico)
