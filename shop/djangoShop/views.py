from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .cart_save import *
from .models import *

from django.http import HttpResponseRedirect


# Create your views here.


def main(request):
    """
    main page
    :param request:
    :return: rendered page
    """

    categories = Category.objects.all()

    return render(request, 'djangoShop/index.html', context={'categories': categories})


def category_detail(request, slug):
    """
    :param request: request obj
    :param slug: unique parameter for each category
    :return: rendered page with category items
    """

    products = Product.objects.filter(category__slug=slug)
    category_name = products[0].category.title
    context = {"products": products, "category_name": category_name}

    return render(request, 'djangoShop/category_items.html', context=context)


def product_detail(request, pk):
    """

    :param request: request obj
    :param slug: unique slug for product
    :return:

    """

    product = Product.objects.get(pk=pk)

    return render(request, 'djangoShop/product_detail.html', context={"product": product})


def add_to_cart(request, pk):
    """

    :param request: obj
    :return: added item to cart
    """
    product = Product.objects.get(pk=pk)
    append_product(request.user.id, product.pk)

    return redirect("/products/{}".format(str(pk)))

def get_cart(request):
    """

    :param request:
    :return: rendered page with user items in cart
    (saved in redis)
    """

    items = get_product(request.user.id)

    objects = []

    for i in items:
        if i:
            result = Product.objects.get(pk=i)
            objects.append(result)


    full_price = 0
    for obj in objects:
        full_price += obj.price

    return render(request, "djangoShop/cart.html", context={"products": objects, "full_price": full_price})


def clean_cart(request):
    """
    Cleans all data from cart for current user
    :param request:
    :return:
    """
    empty_cart(request.user.id)

    return redirect("/get_cart")

