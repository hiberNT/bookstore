from django.urls import include, path
from rest_framework import routers

from order import viewsets

router = routers.SimpleRouter()
router.register(
    r"order", viewsets.OrderViewSet, basename="order"
)  # O urls é configurado pra definirmos o viewset como uma rota do nosso projeto tipo bookstore/order o basename é como queremos apareça na rota

urlpatterns = [
    path("", include(router.urls)),
]
