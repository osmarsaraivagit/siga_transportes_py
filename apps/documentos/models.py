from django.db import models

class Documento(models.Model):
    nome_doc = models.CharField(max_length=80)

    def __str__(self):
        return self.nome_doc
