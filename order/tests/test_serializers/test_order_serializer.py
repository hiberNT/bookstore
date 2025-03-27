from django.test import TestCase

from order.factories import OrderFactory, ProductFactory #cria pedidos ficticios
from order.serializers import OrderSerializer


class TestOrderSerializer(TestCase):
    def setUp(self) -> None:
        self.product_1 = ProductFactory()
        self.product_2 = ProductFactory()

        self.order = OrderFactory(product=(self.product_1, self.product_2)) #Cria um pedido com os dois produtos
        self.order_serializer = OrderSerializer(self.order) #serializando a order aqui, Serializar um produto significa transformar um objeto Python 
        
    def test_order_serializer(self):
        serializer_data = self.order_serializer.data # O .data converte esses dados em um dicionário pronto para ser enviado via API (JSON).
        self.assertEqual( #assertEqual é usado para verificar se um valor obtido em um teste é igual ao valor esperado.
            serializer_data["product"][0]["title"], self.product_1.title)
        self.assertEqual(
            serializer_data["product"][1]["title"], self.product_2.title)