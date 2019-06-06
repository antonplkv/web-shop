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

    name = models.CharField(max_length=150, default="")
    email = models.EmailField(default="dasd@ukr.net")
    city = models.CharField(max_length=100, default="")

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=1)
    total = models.PositiveIntegerField(default=0)
    products = models.TextField()
