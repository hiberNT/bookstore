import json

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from order.factories import OrderFactory, UserFactory
from order.models import Order
from product.factories import CategoryFactory, ProductFactory
from product.models import Product


class TestOrderViewSet(APITestCase):

    client = APIClient()

    def setUp(self):
        self.user = UserFactory()  # criando usuario
        token = Token.objects.create(user=self.user)  # para funcinar a autenticação
        token.save()

        self.category = CategoryFactory(
            title="technology"
        )  # criando categoria com factory
        self.product = ProductFactory(
            title="mouse", price=100, category=[self.category]
        )  # criando um produto e passando que vou criar uma lista[] de categorias pois la no factories product passei o for nas categorias
        self.order = OrderFactory(product=[self.product])

    def test_order(self):
        token = Token.objects.get(
            user__username=self.user.username
        )  # passando o usuario criado ali em cima no setup
        self.client.credentials(  # adicionando as credenciais as chaves do token,fazendo justamente aqui pra que quando passr pelo get pegar esse token
            HTTP_AUTHORIZATION="Token " + token.key
        )
        response = self.client.get(reverse("order-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # fazendo uma revalidação para ve se tudo que criei deu certo
        order_data = json.loads(
            response.content
        )  # carrega o json que recebo do viewset
        print(order_data)
        results = order_data["results"]
        self.assertEqual(results[0]["product"][0]["title"], self.product.title)
        # self.assertEqual(order_data [0]["product"][0]["title"], self.product.title)#comparando o json com o item criado aqui, passa o indice 0
        self.assertEqual(results[0]["product"][0]["price"], self.product.price)
        self.assertEqual(results[0]["product"][0]["active"], self.product.active)
        self.assertEqual(
            results[0]["product"][0]["category"][0]["title"],
            self.category.title,
        )

    def test_create_order(self):  # criando uma nova order
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        user = UserFactory()
        product = ProductFactory()
        data = json.dumps({"products_id": [product.id], "user": user.id})

        response = self.client.post(  # estamos fazendo um post vamos salvar essas infos vamos criar esse produto
            reverse("order-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )  # pra validar se deu certo 201 status do create

        created_order = Order.objects.get(user=user)
