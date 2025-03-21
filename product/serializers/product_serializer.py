from rest_framework import serializers

from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer): 
    category = CategorySerializer(read_only=True, many=True) #lembrando q o serializer estamos apenas espelhado os campos q tao la em model por isso so digitei os campos id,title mas eu quero que o category esteja visivel por isso passei aqui nessa linha o true
    

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "active",
            "category",
        ]