from django.db import models

class Estoque_Produto(models.Model):
    estoque_atual = models.IntegerField()
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Estoque_Negativo(models.Model):
    vendas = models.IntegerField()
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Anuncio_Produto(models.Model):
    estoque_virtual = models.IntegerField()
    nome = models.CharField(max_length=100) 

    def __str__(self):
        return self.nome

class Tabela_Integracao(models.Model):
    qnt = models.IntegerField()
    estq_prod = models.ForeignKey(Estoque_Produto, on_delete=models.CASCADE)
    anun_prod = models.ForeignKey(Anuncio_Produto, on_delete=models.CASCADE) 
