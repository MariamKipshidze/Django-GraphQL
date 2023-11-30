import graphene
from graphene_django import DjangoObjectType, DjangoListField

from product.models import Product, Category


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ('id', 'category', 'title', 'ingredients', 'price')


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'title')


class Query(graphene.ObjectType):
    all_products = DjangoListField(ProductType)
    all_categories = graphene.List(CategoryType)

    @staticmethod
    def resolve_all_products(*_, **__):
        return Product.objects.all()

    @staticmethod
    def resolve_all_categories(*_, **__):
        return Category.objects.all()


schema = graphene.Schema(query=Query)
