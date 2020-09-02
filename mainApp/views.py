from django.shortcuts import get_object_or_404, render
from .models import Product
from django.http import Http404


def index(request):
    return render(request, 'mainApp/index.html')


def store(request):
    return render(request, 'mainApp/store.html')


def products(request, prod_type):
    products_list = Product.objects.filter(product_type=prod_type)
    if products_list.count() == 0:
        raise Http404("We dont have that type of product")
    context = {'products': products_list}
    return render(request, 'mainApp/products.html', context)


def product(request, prod_type, prod_id):
    product = get_object_or_404(Product, id=prod_id)
    context = {"product": product}
    return render(request, 'mainApp/product.html', context)
