from django.db import models

class Clientes(models.Model):
    nome = models.CharField("Nome", max_length=20)
    sobrenome = models.TextField("Sobrenome", max_length=35)
    documento = models.CharField("CPF", max_length=11)
    idade = models.IntegerField("Idade", default=0)
    data_nascimento = models.DateTimeField("Data de nascimento")

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

    def __str__(self):
        return f"{self.nome} - {self.sobrenome} - {self.documento}"
