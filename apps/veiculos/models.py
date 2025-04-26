from django.db import models
from apps.tipos_veiculos.models import TipoVeiculo
from apps.empresas.models import Empresa
from apps.frotas.models import Frota
from apps.situacoes.models import Situacao


class Veiculo(models.Model):
    tipo_veiculo = models.ForeignKey(TipoVeiculo, null=True, on_delete=models.SET_NULL)
    marca = models.CharField(max_length=80, blank=False, null=False)
    modelo = models.CharField(max_length=80, blank=False, null=False)
    ano = models.IntegerField(null=False, blank=True)
    data_fabricacao = models.DateField(null=False, blank=True)
    renavam = models.IntegerField(null=False, blank=True)
    placas = models.CharField(max_length=80, blank=False, null=False)
    datacompra = models.DateField('data', null=False, blank=True)  # Field name made lowercase.
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    empresa = models.ForeignKey(Empresa, null=True, on_delete=models.SET_NULL)
    frota = models.ForeignKey(Frota, null=True, on_delete=models.SET_NULL)
    tipo_aquisicao = models.CharField(max_length=50, blank=False, null=False)
    km_inicial = models.IntegerField(null=False, blank=True)
    situacoes = models.ForeignKey(Situacao, null=True, on_delete=models.SET_NULL)
    obs = models.CharField(max_length=100, blank=False, null=False)


    class Meta:
        db_table = 'veiculo'