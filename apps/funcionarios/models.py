from django.db import models
from apps.cidades.models import Cidade
from apps.estados.models import Estado
from apps.funcao.models import (Funcao)
from apps.situacoes.models import Situacao


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(db_column='CPF', max_length=50)  # Field name made lowercase.
    pis = models.CharField(db_column='PIS', max_length=30)  # Field name made lowercase.
    data_admissao = models.DateField()
    data_demissao = models.DateField()
    salario = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=90)
    fk_cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    fk_estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    funcao = models.ForeignKey(Funcao, null=True, on_delete=models.SET_NULL)
    telefone = models.CharField(max_length=60)
    situacoes = models.ForeignKey(Situacao, null=True, on_delete=models.SET_NULL)
    obs = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nome