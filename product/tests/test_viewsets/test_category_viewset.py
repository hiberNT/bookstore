import json

from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from product.factories import CategoryFactory
from product.models import Category


class CategoryViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title="books")  # criei a categoria

    def test_get_all_category(self):
        response = self.client.get(  # passando o teste com o get
            reverse("category-list", kwargs={"version": "v1"})
        )

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )  # resposta do get status  200 que é oq dar quando esta ok

        category_data = json.loads(
            response.content
        )  # se passou do get agora cria o data como json para fazer alguma validações

        self.assertEqual(
            category_data["results"][0]["title"], self.category.title
        )  # uma vez que tenho os dados em json podemos testar o title criado, comparando o category data que pegou a resposta em json e trasformou em biblioteca com o category criado no set up

    def test_create_category(self):
        # criando nova categoria
        data = json.dumps({"title": "technology"})

        response = self.client.post(
            reverse("category-list", kwargs={"version": "v1"}),
            data=data,  # o data é a informação que estamos mandando pro api q vai ser criado
            content_type="application/json",
        )

        # import pdb; pdb.set_trace() #debug de python

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_category = Category.objects.get(
            title="technology"
        )  # aqui o teste para confirmar que crou a categoria

        self.assertEqual(
            created_category.title, "technology"
        )  # testando se foi a mesma informação q passamos
