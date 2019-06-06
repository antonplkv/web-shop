"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import *
urlpatterns = [

    path('', main, name='main-url'),
    path('category/<str:slug>', category_detail, name='category-url'),
    path('products/<int:pk>', product_detail, name='product-url'),
    path('add_to_cart/<int:pk>', add_to_cart, name='add_to_cart_url'),
    path('get_cart', get_cart, name='cart-url'),
    path('clean_cart', clean_cart, name='cleancart-url'),
    path('auth/', include('auth_app.urls')),
    path('make_order/', make_order, name='order-form-url'),
    path('account/', my_account, name='account-url'),
    path('order_detail/<int:pk>', order_detail, name='order-detail-url'),

]
