from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=50, null=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    descricao=models.CharField(max_length=200, null=False)
    quantidade=models.IntegerField(null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False)
    # imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)

    def __str__(self):
        return self.nome