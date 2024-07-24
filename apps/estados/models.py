from django.db import models


class Estado(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome do Estado")

    def __str__(self):
        return self.nome
