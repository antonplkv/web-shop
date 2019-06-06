from django.db import models
from django.contrib.auth.models import User

from .storage import OverwriteStorage
# Create your models here.


def generate_path(instance, filename):
    return "{0}/{1}".format(instance.category, filename)


class Category(models.Model):
    """
    Model that describes category
    """

    title = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return str(self.title)


class Product(models.Model):
    """
    Model that describes product
    """

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    body = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(storage=OverwriteStorage(), upload_to=generate_path, unique=True)

    def __str__(self):
        return str(self.pk)

class Cart(models.Model):
    """
    Basket сontains products
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class Order(models.Model):

    name = models.CharField(max_length=150)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.PositiveIntegerField()
    products = models.TextField()
