from django.contrib import admin

from consulta.models import Consulta

class detConsulta(admin.ModelAdmin):
    list_display = ['id', 'data', 'hora', 'paciente', 'medico']
    list_filter = ['data', 'hora', 'paciente', 'medico']
    search_fields = ['data', 'hora', 'paciente', 'medico']

admin.site.register(Consulta, detConsulta)
