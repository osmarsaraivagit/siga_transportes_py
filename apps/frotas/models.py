from django.db import models
from apps.empresas.models import Empresa
from apps.situacoes.models import Situacao

class Frota(models.Model):
    nome_frota = models.CharField(max_length=20)
    fk_empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    fk_situacao = models.ForeignKey(Situacao, on_delete=models.PROTECT)
    data_cadastro = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.nome