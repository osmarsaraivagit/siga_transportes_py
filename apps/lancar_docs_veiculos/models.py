from django.db import models
from apps.veiculos.models import Veiculo
from apps.empresas.models import Empresa


class LancarDocsVeiculos(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=False)
    data_realizado = models.DateField(null=False, blank=True)
    data_vencimento = models.DateField(null=False, blank=True)
    empresa = models.ForeignKey(Empresa, null=True, on_delete=models.SET_NULL)
    veiculo = models.ForeignKey(Veiculo, null=True, on_delete=models.SET_NULL)
    obs = models.CharField(max_length=100, blank=False, null=False)
    status = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.nome


    class Meta:
        db_table = 'lancar_doc_veiculo'