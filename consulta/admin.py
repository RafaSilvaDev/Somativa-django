from django.contrib import admin

from consulta.models import Consulta

class detConsulta(admin.ModelAdmin):
    list_display = ['id', 'data', 'hora', 'descricao', 'paciente', 'medico']
    list_filter = ['data', 'hora', 'descricao', 'paciente', 'medico']
    search_fields = ['data', 'hora', 'descricao', 'paciente', 'medico']

admin.site.register(Consulta, detConsulta)
