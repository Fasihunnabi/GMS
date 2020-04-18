from django.shortcuts import render
from .models import Product, ProductImage, ProductCategory

# Create your views here.


def shop(request):
    products_list = Product.objects.all()
    print(products_list)
    print(products_list)

    product_categories = ProductCategory.objects.all()

    context = {
        'products_list': products_list,
        'product_categories': product_categories,
    }

    return render(request, "base/index.html", context)


def products_by_category(request, slug):
    print(slug)

    category = ProductCategory.objects.get(name=slug)
    print(category)
    print(category)
    print(category)
    print(category)

    products_list = Product.objects.filter(category=category.id)

    context = {
        'products_list': products_list,
        'category': category,
    }

    return render(request, "products/products.html", context)


def product_detail(request, slug):
    product_object = Product.objects.get(id=slug)

    context = {
        'product_object': product_object,
    }

    return render(request, "product_description.html", context)


def list_all_products(request):

    products_list = Product.objects.all()

    context = {
        'products_list': products_list,
    }

    return render(request, "products/all_products_listing.html", context)


def product_images(request):
    pass

