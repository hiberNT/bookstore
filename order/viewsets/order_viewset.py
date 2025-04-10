#é a função que fica na porta de entrada da nossa aplicação , tem q definir qual o serialaizer e qual queryset sempre
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication] #add segurança assim so acessa os produtos que tem autenticação autorizada
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer #definindo o serializer
    queryset = Order.objects.all().order_by("id") #definir o queryset