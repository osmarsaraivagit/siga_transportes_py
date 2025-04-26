from django.db import models

class Situacao(models.Model):

    tipo_nome = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo_nome

