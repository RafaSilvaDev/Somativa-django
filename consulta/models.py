from django.db import models
from medico.models import Medico

class Consulta(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    paciente = models.TextField(max_length=100, null=True, blank=True)
    descricao = models.TextField(max_length=200, null=True, blank=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    # exame = models.TextField(max_length=100)

    def __str__(self):
        return self.paciente, self.medico.nome
