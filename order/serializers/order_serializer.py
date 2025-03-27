from rest_framework import serializers

from order.models import Order
from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer): #model serializer vai extender nossos modelos vai trabalhar em conjunto com o model que esta declarado la em baixo, dai ele já tem diversasa funções já prontas para trabalhar com esse modelo, função de criação, atualização... 
    product = ProductSerializer(read_only=True, many=True)
    products_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, many=True) #seguindo uma logica de quando criamos uma order de uma loja online, quando é criada n criamos novos produtos eles ja exisetem entao basicamente oq fazemos aqui, uma vez que fazemos uma compra e tem varios pedidos dentro do carrinho e efetuamos o pagamento desses pedidos nao estamos criando o produto ele ja existia,entao ele associa a order ao usuario ele cria uma orden mas os produtos ja existem so pega uma referencia aos produtos q foram criados por isso é criado id imagina que tem mais de 1000 produtos cadastrados o django n vai puxar tudo ele so tras uma referencia desses, dai so no momento que criarmos a order la no carrinho o django pega pelos id que nos vamos informar dentro do carrinho  
    total = serializers.SerializerMethodField() #serializer é uma extenção a gente pode manter o que tenho no meu model que vai ser o que vou exibir no serializer e tambem posso extender algo que o serializer permite no caso aqui criei total sem precisar ter q ir la em models passar ele, mas caso quisermos sobreescrever algo o model serializer permite oq estou fazendo aqui o
    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()]) # esse methodfield estou passando pro django que quero criar um metodo que é esse get total e dentro desse get faço o q eu quiser que caso é uma soma de todas as compras
        return total

    class Meta:
        model = Order
        fields = ["product", "total", "user", "products_id"]
        extra_kwargs = {"product": {"required": False}}
               
    def create(self, validated_data): #Esse método é chamado quando o serializer recebe dados válidos e precisa criar um novo objeto no banco. validated_data contém os dados que foram enviados na requisição e passaram pela validação do serializer.
        product_data = validated_data.pop("products_id") #Pega a lista de produtos (IDs) enviados na requisição. Usa pop() para remover products_id de validated_data (evitando erro, pois products_id não está no modelo Order).
        user_data = validated_data.pop("user")#Pega o usuário que está fazendo a compra. O usuário está na requisição, mas não precisa ser salvo como parte de validated_data, então também é removido.

        order = Order.objects.create(user=user_data) #Cria um novo objeto Order, passando apenas o user (sem os produtos ainda).O objeto é salvo no banco automaticamente.
        for product in product_data: #Percorre a lista de produtos (products_id) recebidos na requisição. Percorre a lista de produtos (products_id) recebidos na requisição.O método .add() serve para adicionar relações muitos-para-muitos entre Order e Product.
            order.product.add(product)

        return order