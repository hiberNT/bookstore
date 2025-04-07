from django.db import models
from django.contrib.auth.models import User

from product.models import Product


class Order(models.Model): #Faz com que a classe herde de models.Model, tornando-a um modelo do Django (ou seja, será uma tabela no banco de dados).
    product = models.ManyToManyField(Product, blank=False) #Um pedido pode ter vários produtos.,Um produto pode estar em vários pedidos
    user = models.ForeignKey(User, on_delete=models.CASCADE) #Um usuário pode fazer vários pedidos., Cada pedido pertence a um único usuário on_delete=models.CASCADE: Se a categoria for deletada, todos os livros dessa categoria também serão removidos. 