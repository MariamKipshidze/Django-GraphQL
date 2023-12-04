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


class CategoryMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, _, __, title: str):
        category = Category(title=title)
        category.save()
        return CategoryMutation(category=category)


class Mutation(graphene.ObjectType):
    """
       Request Format - creating category object:
       mutation {
          updateCategory(title: "new category"){
            category{
              title
                }
            }
        }
    """
    update_category = CategoryMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
