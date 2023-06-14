from django.db import models
from django.utils.timezone import now
from animais.models import Animais
from clientes.models import Clientes


class Adocoes(models.Model):
    animal = models.ForeignKey(Animais, on_delete=models.CASCADE, default=1)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE,default=1)
    dataAdocao = models.DateTimeField("Data de adoção", null=False, default=now)

    
    class Meta:
        verbose_name = 'Adoção'
        verbose_name_plural = 'Adoções'
        ordering = ['id']

    def __str__(self):
      return f"{self.animal} - {self.cliente} - {self.dataAdocao}"
        