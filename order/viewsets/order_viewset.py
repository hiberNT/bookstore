#é a função que fica na porta de entrada da nossa aplicação , tem q definir qual o serialaizer e qual queryset sempre
from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):

    serializer_class = OrderSerializer #definindo o serializer
    queryset = Order.objects.all().order_by("id") #definir o queryset