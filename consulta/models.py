from django.db import models

from medico.models import Medico

class Consulta(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    paciente = models.TextField(max_length=100)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    def __str__(self):
        return self.paciente.nome
