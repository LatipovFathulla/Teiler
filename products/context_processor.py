from carousel.models import CarouselModel
from help.models import HelpCategory, HelpSubcategory
from user.forms import SendEmailForm
from products.models import CategoryModel, ProductModel, BrandModel, ColorModel, SubCategoryModel


def product_categories(request):
    categories = CategoryModel.objects.order_by('pk')
    subcategories = SubCategoryModel.objects.order_by('pk')
    products = ProductModel.objects.order_by('pk')
    brands = BrandModel.objects.order_by('pk')
    colors = ColorModel.objects.order_by('pk')
    carousels = CarouselModel.objects.order_by('pk')
    help_categories = HelpCategory.objects.order_by('pk')
    help_subcategories = HelpSubcategory.objects.order_by('pk')
    random_products = ProductModel.objects.order_by('?')

    return {
        'categories': categories,
        'subcategories': subcategories,
        'products': products,
        'brands': brands,
        'colors': colors,
        'carousels': carousels,
        'help_categories': help_categories,
        'help_subcategories': help_subcategories,
        'random_products': random_products
    }


def subscription_form(request):
    return {'subscription_form': SendEmailForm()}
