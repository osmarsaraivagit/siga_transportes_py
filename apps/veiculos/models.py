from django.db import models
from apps.tipos_veiculos.models import TipoVeiculo
from apps.empresas.models import Empresa
from apps.frotas.models import Frota
from apps.situacoes.models import Situacao


class Veiculo(models.Model):
    fk_tipo_veiculo = models.ForeignKey(TipoVeiculo, on_delete=models.PROTECT)
    marca = models.CharField(max_length=80)
    modelo = models.CharField(max_length=80)
    placas = models.CharField(max_length=80)
    datacompra = models.DateField(db_column='dataCompra')  # Field name made lowercase.
    fk_empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    fk_frota = models.ForeignKey(Frota, on_delete=models.PROTECT)
    tipo_aquisicao = models.CharField(max_length=50)
    km_inicial = models.IntegerField()
    fk_situacao = models.ForeignKey(Situacao, on_delete=models.PROTECT)