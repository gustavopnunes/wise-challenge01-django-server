from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    preco = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
