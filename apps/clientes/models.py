from django.db import models
from apps.cidades.models import Cidade
from apps.estados.models import Estado


class Cliente(models.Model):
    nome = models.CharField(max_length=80)
    cnpj = models.CharField(db_column='CNPJ', max_length=60)  # Field name made lowercase.
    ie = models.CharField(max_length=60)
    outro_documento = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=80)
    telefone = models.CharField(max_length=60)
    data_cadastro = models.DateField()
    fk_cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    fk_estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome