from rest_framework import serializers

from order.models import Order
from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer): #model serializer vai extender nossos modelos vai trabalhar em conjunto com o model que esta declarado la em baixo, dai ele já tem diversasa funções já prontas para trabalhar com esse modelo, função de criação, atualização... 
    product = ProductSerializer(read_only=True, many=True)
    products_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True, many=True
    )
    total = serializers.SerializerMethodField() #serializer é uma extenção a gente pode manter o que tenho no meu model que vai ser o que vou exibir no sirializer e tambem posso extender algo que o serializer permite no caso aqui criei total sem precisar ter q ir la em models passar ele, mas caso quisermos sobreescrever algo o model serializer permite oq estou fazendo aqui o
    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()]) # esse methodfield estou passando pro django que quero criar um metodo que é esse get total e dentro desse get faço o q eu quiser que caso é uma soma de todas as compras
        return total

    class Meta:
        model = Order
        fields = ["product", "total"]