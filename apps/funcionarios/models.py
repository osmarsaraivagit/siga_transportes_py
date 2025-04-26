from django.db import models
from apps.cidades.models import Cidade
from apps.estados.models import Estado


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(db_column='CPF', max_length=50)  # Field name made lowercase.
    pis = models.CharField(db_column='PIS', max_length=30)  # Field name made lowercase.
    data_admissao = models.DateField()
    data_demissao = models.DateField()
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=90)
    fk_cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    fk_estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    funcao = models.CharField(max_length=60)
    telefone = models.CharField(max_length=60)

    def __str__(self):
        return self.nome