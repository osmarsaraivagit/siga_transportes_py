from django.db import models
from apps.lancar_viagem.models import LancarViagem
from apps.plano_contas.models import PlanoConta
from apps.forma_pagamento.models import (FormaPagamento)


class LancarAcertoViagem(models.Model):
    lancar_viagem = models.ForeignKey(LancarViagem, on_delete=models.POR)
    data_acerto = models.DateField(null=False, blank=True)
    km_final = models.IntegerField(null=False, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)
    historico = models.CharField(max_length=100, blank=False, null=False)
    plano_conta = models.ForeignKey(PlanoConta, null=False, on_delete=models.SET_NULL)
    forma_pagamento = models.ForeignKey(FormaPagamento, null=False, on_delete=models.SET_NULL)
    status = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.data_acerto


    class Meta:

        db_table = 'lancar_acerto_viagem'

