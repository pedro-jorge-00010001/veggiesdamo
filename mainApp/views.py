from django.shortcuts import get_object_or_404, render
from .models import Product
from django.http import HttpResponse


def index(request):
    return render(request, 'mainApp/index.html')


def store(request):
    return render(request, 'mainApp/store.html')


def products(request, prod_type):
    products_list = Product.objects.filter(product_type=prod_type)
    context = {'products': products_list}
    return render(request, 'mainApp/products.html', context)


def product(request, prod_type, prod_id):
    product = get_object_or_404(Product, id=prod_id)
    context = {"product": product}
    return render(request, 'mainApp/product.html', context)