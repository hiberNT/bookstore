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

    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for product in extracted:
                self.product.add(product)

    class Meta:
        model = Order