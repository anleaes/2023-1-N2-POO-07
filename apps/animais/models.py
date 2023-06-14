from django.db import models

class Animais(models.Model):
    especie = models.CharField("Espécie")
    name = models.CharField("Nome")
    raca = models.CharField("Raça")
    idade = models.IntegerField("Idade")

    
    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'
        ordering =['id']

    def __str__(self):
         return f"{self.especie}-{self.nome}-{self.idade}"