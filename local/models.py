from django.db import models


class Locais(models.Model):
    nome = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
      verbose_name_plural = "Locais"

class Espaco(models.Model):
    nome = models.CharField(max_length=150)
    local = models.ForeignKey(Locais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
