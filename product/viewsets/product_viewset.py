from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by(
            "id"
        )  # outra forma de fazer o queryset Pega todas as categorias do banco de dados. Ordena os resultados pelo campo id em ordem crescente
