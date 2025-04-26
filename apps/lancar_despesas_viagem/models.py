from django.db import models
from apps.lancar_viagem.models import LancarViagem
from apps.plano_contas.models import PlanoConta
from apps.documentos.models import Documento
from apps.empresas.models import Empresa
from apps.fornecedores.models import Fornecedor
from apps.forma_pagamento.models import (FormaPagamento)

class LancarDespesasViagem(models.Model):
    lancar_viagem = models.ForeignKey(LancarViagem, null=True, on_delete=models.SET_NULL)
    data = models.DateField(null=False, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)
    historico = models.CharField(max_length=100, blank=False, null=False)
    plano_conta = models.ForeignKey(PlanoConta, null=True, on_delete=models.SET_NULL)
    documento = models.ForeignKey(Documento, null=True, on_delete=models.SET_NULL)
    empresa = models.ForeignKey(Empresa, null=True, on_delete=models.SET_NULL)
    fornecedor = models.ForeignKey(Fornecedor, null=True, on_delete=models.SET_NULL)
    forma_pagamento = models.ForeignKey(FormaPagamento, null=False, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'lancar_financeiro_viagem'