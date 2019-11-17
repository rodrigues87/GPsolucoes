from django.db import models

from local.models import Locais, Espaco


class Problema(models.Model):
    descricao = models.CharField(max_length=150, null=True, blank=True)
    espaco = models.ForeignKey(Espaco,on_delete=models.CASCADE)
    solucionado = models.BooleanField(default=False)
