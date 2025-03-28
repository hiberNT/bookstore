import json

from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from order.factories import UserFactory
from product.factories import CategoryFactory, ProductFactory
from product.models import Product


class TestProductViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()#criando usuario
        token = Token.objects.create(user=self.user)# para funcinar a autenticação
        token.save() 
        
        self.product = ProductFactory(#criando produto
            title="pro controller",
            price=200.00,
        )

    def test_get_all_product(self): #testando se os produtos estao listados
        token = Token.objects.get(user__username=self.user.username)#passando o usuario criado ali em cima no setup
        self.client.credentials(#adicionando as credenciais as chaves do token,fazendo justamente aqui pra que quando passr pelo get pegar esse token
            HTTP_AUTHORIZATION="Token " + token.key)
        response = self.client.get(
            reverse("product-list", kwargs={"version": "v1"}) #listando os produtos que criamos a cima no setUp
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product_data = json.loads(response.content)

        self.assertEqual(product_data[0]["title"], self.product.title)
        self.assertEqual(product_data[0]["price"], self.product.price)
        self.assertEqual(product_data[0]["active"], self.product.active)

    def test_create_product(self): #criando produto novo
        category = CategoryFactory()
        data = json.dumps(
            {"title": "notebook", "price": 800.00,
                "categories_id": [category.id]}
        )

        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data=data, #o data seria as informaçoes do nosso payload informaçoes que estamos enviando peo viewset
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_product = Product.objects.get(title="notebook")

        self.assertEqual(created_product.title, "notebook") #validando se esses saomos itens que esta no nosso payload
        self.assertEqual(created_product.price, 800.00)