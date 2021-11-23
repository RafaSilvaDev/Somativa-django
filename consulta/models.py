from django.db import models

from medico.models import Medico
from paciente.models import Paciente

class Consulta(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    def __str__(self):
        return self.paciente.nome
