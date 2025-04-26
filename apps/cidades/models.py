from django.db import models


class Cidade(models.Model):
    nome = models.CharField(max_length=50, help_text="Nome da cidade")

    def __str__(self):
        return self.nome