from django.db import models


class TipoVeiculo(models.Model):
    tipo_veiculo = models.CharField(max_length=30)

    def __str__(self):
        return self.tipo_veiculo