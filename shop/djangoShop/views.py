from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .cart_save import *
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from django.http import HttpResponseRedirect
from .utils import tracker

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
    if request.user.is_authenticated:
        user_key = str(request.user.id)
    else:
        user_key = str(tracker(request))

    append_product(user_key, product.id)

    return redirect("/products/{}".format(str(pk)))

def get_cart(request):
    """

    :param request:
    :return: rendered page with user items in cart
    (saved in redis)
    """

    if request.user.is_authenticated:
        user_key = str(request.user.id)
    else:
        user_key = str(tracker(request))

    items = get_product(user_key)
    objects = []
    print(items)
    for i in items:
        if i:
            result = Product.objects.get(pk=i)
            objects.append(result)

    full_price = get_full_price(objects)

    return render(request, "djangoShop/cart.html", context={"products": objects, "full_price": full_price})


def clean_cart(request):
    """
    Cleans all data from cart for current user
    :param request:
    :return:
    """

    if request.user.is_authenticated:
        user_key = str(request.user.id)
    else:
        user_key = tracker(request)

    empty_cart(user_key)

    return redirect("/get_cart")

@login_required(login_url="/auth/login/")
def make_order(request):
    """
    Here we getting order info from user
    :param request:
    :return:
    """

    if request.method == "POST":
        form = OrderForm(data=request.POST)
        if form.is_valid():

            items = get_product(request.user.id)
            objects = []
            for i in items:
                if i:
                    result = Product.objects.get(pk=i)
                    objects.append(result)


            name = form.cleaned_data["name"]
            city = form.cleaned_data["city"]

            user = request
            total_price = get_full_price(objects)
            products = items

            order = Order.objects.create(name=name, email=user.user.email,
                                         city=city, user=user.user, total=total_price,
                                         products=products)
            order.save()

            return redirect("/")

    else:
        form = OrderForm()
        return render(request, 'djangoShop/form.html', {'form': form})



def my_account(request):
    """
    Displays info about latest orders of this user
    :param request:
    :return:
    """
    my_orders = Order.objects.filter(user=request.user)
    return render(request, 'djangoShop/account.html', context={"orders": my_orders})


def order_detail(request, pk):
    """
    Functions shows full info about selected
    order
    :param request:
    :return:
    """

    order = Order.objects.get(pk=pk)



    objects = []
    products = order.products.replace("'", "").replace("[", '').replace("]", '').replace(" ", '').split(',')

    print(products)
    for i in products:
        if i:
            result = Product.objects.get(pk=i)
            objects.append(result)


    print(objects)
    full_price = get_full_price(objects)

    return render(request, 'djangoShop/order_detail.html',
                  context={"order": order, "products": objects,
                           'full_price': full_price})