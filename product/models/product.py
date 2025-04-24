from django.db import models

from product.models import Category


class Product(models.Model):  # modelo de produto
    title = models.CharField(
        max_length=100
    )  # Cria um campo de texto curto (CharField) para armazenar o título do produto.
    description = models.TextField(
        max_length=500, blank=True, null=True
    )  # Armazena um texto maior (até 500 caracteres)., blank=True → O campo pode ser deixado vazio ao cadastrar um produto.
    price = models.PositiveIntegerField(
        null=True
    )  # Armazena apenas números inteiros positivos.
    active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, blank=True)
