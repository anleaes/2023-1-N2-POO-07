from django.db import models

class Animais(models.Model):
    especie = models.CharField("Espécie", max_length=20)
    name = models.CharField("Nome", max_length=20)
    raca = models.CharField("Raça", max_length=20)
    idade = models.IntegerField("Idade")

    
    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'
        ordering =['id']

    def __str__(self):
         return f"{self.especie}-{self.nome}-{self.idade}"