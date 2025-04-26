from django.db import models


class Estado(models.Model):
    nome = models.CharField(max_length=30, help_text="Nome do Estado")
    pais = models.CharField(max_length=2, help_text="Nome do País em sigla")

    def __str__(self):
        return self.nome
