from django.db import models
from animais.models import Animais

class PorteAnimal(models.Model):
    altura = models.FloatField("altura animal")
    peso = models.FloatField("peso animal")
    animal = models.ForeignKey(Animais, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'PorteAnimal'
        verbose_name_plural = 'PorteAnimais'
        ordering =['id']

    def __str__(self):
        return f"{self.altura}-{self.peso}"