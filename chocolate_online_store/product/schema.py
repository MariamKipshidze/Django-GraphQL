import graphene
from graphene_django import DjangoObjectType

from product.models import Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ('id', 'title')


class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)

    @staticmethod
    def resolve_all_products(*_, **__):
        return Product.objects.all()


schema = graphene.Schema(query=Query)