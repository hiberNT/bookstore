import factory

from product.models import Category, Product


class CategoryFactory(factory.django.DjangoModelFactory): #Basicamente estamos fazendo testes dai fazemos esses itens falsos mas com base do q foi contruido em category e product
    title = factory.Faker("pystr")
    slug = factory.Faker("pystr")
    description = factory.Faker("pystr")
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker("pyint")
    category = factory.LazyAttribute(CategoryFactory) #esse lazy é para fazermos as anotações que estao abaixo, uma vez que instanciou p Product Factory criou nosso objetos essa anotação faz , foi informado alguma categoria na construção do factorie se foi o extract verifica se o categorie foi instanciado se ele foi vai fazer uma interação vai adicionar as categorias q fora declaradas na instanca da nossa categoria
    title = factory.Faker("pystr")

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.category.add(category)#o self é o product dai dentro o product tem a category criada como manyTomany, dai o for passa por uma lista de categorias dai faz a interação pra cada categoria to passando uma categoria individual para o produto q nois criamos

    class Meta:
        model = Product