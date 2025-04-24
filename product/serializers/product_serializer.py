from rest_framework import serializers

from product.models.product import Product, Category
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(
        read_only=True, many=True
    )  # lembrando q o serializer estamos apenas espelhado os campos q tao la em model por isso so digitei os campos id,title mas eu quero que o category esteja visivel por isso passei aqui nessa linha o true
    categories_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, many=True
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "active",
            "category",
            "categories_id",
        ]

    def create(self, validated_data):
        category_data = validated_data.pop("categories_id")

        product = Product.objects.create(**validated_data)
        for category in category_data:
            product.category.add(category)

        return product
