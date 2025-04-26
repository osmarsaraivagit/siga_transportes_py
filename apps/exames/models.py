from django.db import models


class Exame(models.Model):
    nome = models.CharField(max_length=40, blank=False, null=False)
    cid = models.CharField(max_length=40, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'exame'