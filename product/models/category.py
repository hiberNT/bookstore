from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(
        unique=True
    )  # Cria um SlugField, que é um campo usado em URLs para representar a categoria de forma amigável Exemplo: Se a categoria for "Eletrônicos", o slug pode ser "eletronicos", unique=True → Garante que não pode haver duas categorias com o mesmo slug.
    description = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):  # Este método retorna o título da categoria como uma string.
        return self.title
