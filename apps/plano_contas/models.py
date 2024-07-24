from django.db import models

class PlanoConta(models.Model):
    conta = models.IntegerField()
    tipo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=20)
    subconta = models.IntegerField()
    sigla_situacao = models.CharField(max_length=1)
    saldo = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self):
        return self.conta