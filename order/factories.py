import factory
from django.contrib.auth.models import User #n construimos o usuario to usando o modelo fake q o django fornece

from order.models import Order
from product.factories import ProductFactory


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("pystr")
    username = factory.Faker("pystr")

    class Meta:
        model = User


class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    @factory.post_generation #uma vez que criamos o factory podemos interceptar a criação de um objeto que é esse o caso aqui
    def product(self, create, extracted, **kwargs): #esse self é o Order
        if not create:
            return

        if extracted:
            for product in extracted:
                self.product.add(product) #oq estou passando aqui é que quero adicionar produtos dentro da minha order, la na criação do order o product foi criado como manyTomany por isso passamos o for para passar por todos os produtos

    class Meta:
        model = Order