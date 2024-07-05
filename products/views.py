from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, FormView
from django.db.models import Max, Min, Avg, Sum, Count
from django.http import JsonResponse
from rest_framework.response import Response

from cart.forms import CartAddProductForm
from products import models, forms
from products.forms import ReviewForm
from products.models import ProductModel, ProductAttributes
from cart.cart import Cart
from products.utils import get_wishlist_data, get_cart_data


class HomeTemplate(TemplateView):
    template_name = 'index.html'

    def get_object(self, queryset=None):
        obj, created = self.model.objects.get_or_create(bar='foo bar baz')
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()

        return context


class ProductTemplate(ListView):
    template_name = 'products.html'
    context_object_name = 'products'

    def get_object(self, queryset=None):
        obj, created = self.model.objects.get_or_create(bar='foo bar baz')
        return obj

    def get_queryset(self, ):
        q = self.request.GET.get('q', '')
        price = self.request.GET.get('price')
        category = self.request.GET.get('category')
        subcategory = self.request.GET.get('subcategory')

        filters = {}

        if q:
            filters['title__icontains'] = q

        if category:
            filters['category_id'] = category

        if subcategory:
            filters['subcategory_id'] = subcategory

        if price:
            price_from, price_to = price.split(';')
            filters['price__gte'] = price_from
            filters['price__lte'] = price_to

        return ProductModel.objects.filter(**filters).order_by('pk')[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        context['cart'] = Cart(self.request)
        context['total_data'] = ProductModel.objects.count()
        context['min_price'], context['max_price'] = ProductModel.objects.aggregate(
            Min('real_price'),
            Max('real_price')
        ).values()

        return context


class ProductDetailView(DetailView):
    template_name = 'shop/product/detail.html'
    model = ProductModel
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        context['related'] = ProductModel.objects.order_by('-pk')
        context['colors'] = ProductAttributes.objects.all().values('color__id', 'color__code').distinct()
        return context

    def add_to_object(request, pk):
        try:
            object = ProductModel.objects.get(pk=pk)
        except ProductModel.DoesNotExist:
            return Response(data={'status': False})
        cart = request.session.get('cart', [])
        if object.pk in cart:
            cart.remove(object.pk)
            data = {'status': True, 'added': False}
        else:
            cart.append(object.pk)
            data = {'status': True, 'added': True}
        request.session['cart'] = cart

        data['cart_len'] = get_cart_data(cart)
        return JsonResponse(data)


class ProductDeleteView(DeleteView):
    model = ProductModel
    success_url = "/"
    template_name = "basket.html"


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST, request.FILES)
        product = ProductModel.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.product = product
            form.image = request.FILES['image']
            form.save()
            print(request.POST)
        return redirect("/")


# def add_review(request, pk):
#     if request.method == 'POST':
#         product = ProductModel.objects.get(pk=pk)
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save(commit=False)
#             form.product = product
#             form.save()
#     return redirect('/')


class WishlistModelListView(ListView):
    template_name = 'favs.html'
    paginate_by = 7

    def get_queryset(self):
        return ProductModel.get_from_wishlist(self.request)


def add_to_wishlist(request, pk):
    try:
        product = ProductModel.objects.get(pk=pk)
    except ProductModel.DoesNotExist:
        return Response(data={'status': False})
    wishlist = request.session.get('wishlist', [])
    if product.pk in wishlist:
        wishlist.remove(product.pk)
        data = {'status': True, 'added': False}
    else:
        wishlist.append(product.pk)
        data = {'status': True, 'added': True}
    request.session['wishlist'] = wishlist

    data['wishlist_len'] = get_wishlist_data(wishlist)
    return JsonResponse(data)


class CartModelListView(ListView):
    template_name = 'basket.html'
    paginate_by = 7

    def get_queryset(self):
        return ProductModel.get_from_cart(self.request)


def load_more_data(request):
    offset = int(request.GET['offset'])
    limit = int(request.GET['limit'])
    data = ProductModel.objects.all().order_by('id')[offset:offset+limit]
    t = render_to_string('layouts/product-block.html', {'data': data})
    return JsonResponse({'data': t})


def add_to_cart(request, pk):
    try:
        product = ProductModel.objects.get(pk=pk)
    except ProductModel.DoesNotExist:
        return Response(data={'status': False})
    cart = request.session.get('cart', [])
    if product.pk in cart:
        cart.remove(product.pk)
        data = {'status': True, 'added': False}
    else:
        cart.append(product.pk)
        data = {'status': True, 'added': True}
    request.session['cart'] = cart

    data['cart_len'] = get_cart_data(cart)
    return JsonResponse(data)


@login_required
def create_carts(request, pk):
    # product = get_object_or_404(ProductModel, pk=pk)
    # cart = request.session.get('cart', [])
    #
    # if request.user in product.cart.all():
    #     product.cart.remove(request.user)
    # else:
    #     product.cart.add(request.user)
    #
    # product.save()
    #
    # return redirect('order')
    pass


class AboutTemplateView(TemplateView):
    template_name = 'about.html'


class ContactTemplateView(TemplateView):
    template_name = 'contacts.html'


class OrderTemplateView(ListView):
    template_name = 'order.html'

    def get_queryset(self):
        return ProductModel.get_from_cart(self.request)


class ArticleTemplateView(TemplateView):
    template_name = 'articles.html'
