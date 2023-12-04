import graphene
from django.core.exceptions import ObjectDoesNotExist
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
        category_id = graphene.ID(required=False)
        title = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, _, __, title: str, category_id: int = None):
        if not category_id:
            category = Category(title=title)
            category.save()
        else:
            category = Category.objects.filter(id=category_id).first()
            if category:
                category.title = title
                category.save()
                # if we need to delete
                # category.delete()
            else:
                raise ObjectDoesNotExist
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

       Request Format - updating category object:
       mutation {
          updateCategory(title: "category 6", categoryId: 6){
            category{
              title
                }
             }
        }
    """
    update_category = CategoryMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
