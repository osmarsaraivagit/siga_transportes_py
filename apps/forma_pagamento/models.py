from django.db import models

class FormaPagamento(models.Model):

    tipo = models.CharField(max_length=100, blank=False, null=False)


    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'forma_pagamento'
