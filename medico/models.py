from django.db import models



class Medico(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    # agenda = models.Choices()
    foto = models.ImageField(upload_to='media/medicos/fotos', null=True, blank=True)

    def __str__(self):
        return self.nome