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
    get_product = graphene.Field(ProductType, product_id=graphene.Int())

    """
    Request Format:
    {
      allProducts{
        id
        category{
          id 
          title
        }
      }
    }
    """
    @staticmethod
    def resolve_all_products(*_, **__):
        return Product.objects.all()

    @staticmethod
    def resolve_all_categories(*_, **__):
        return Category.objects.all()

    """
    Request Format:
    {
      getProduct(productId:1){
        id
        category{
          id 
          title
        }
      }
    }
    """
    def resolve_get_product(self, _, product_id: int):
        return Product.objects.get(pk=product_id)


schema = graphene.Schema(query=Query)
