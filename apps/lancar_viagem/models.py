from django.db import models
from apps.frotas.models import Frota
from apps.funcionarios.models import Funcionario
from apps.origem.models import Origem
from apps.destino.models import Destino
from apps.empresas.models import Empresa


class LancarViagem(models.Model):
    crtc = models.CharField(max_length=30, blank=False, null=False)
    data = models.DateField(null=False, blank=True)
    frota = models.ForeignKey(Frota, null=True, on_delete=models.SET_NULL)
    motorista = models.ForeignKey(Funcionario, null=True, on_delete=models.SET_NULL)
    origem = models.ForeignKey(Origem, null=True, on_delete=models.SET_NULL)
    destino = models.ForeignKey(Destino, null=True, on_delete=models.SET_NULL)
    frete = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)
    kminicial = models.IntegerField(db_column='kmInicial')  # Field name made lowercase.
    litragem = models.FloatField(null=False, blank=True)
    qtdeveiculos = models.IntegerField(null=False, blank=True)
    fk_empresa = models.ForeignKey(Empresa, related_name='empresa', null=True, on_delete=models.CASCADE)
    obs = models.CharField(max_length=100, blank=False, null=False)
    status = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.crtc


    class Meta:
        db_table = 'lancar_viagem'