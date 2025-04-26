from django.db import models
from apps.cidades.models import Cidade
from apps.estados.models import Estado
from apps.pais.models import Pais

class Destino(models.Model):
    cidade = models.ForeignKey(Cidade, null=True, on_delete=models.SET_NULL)
    estado = models.ForeignKey(Estado,null=True, on_delete=models.SET_NULL)
    pais = models.ForeignKey(Pais, null=True, on_delete=models.SET_NULL)

    class Meta:

        db_table = 'destino'