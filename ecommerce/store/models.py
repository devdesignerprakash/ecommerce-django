from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price=models.IntegerField()
    images=models.ImageField(upload_to='photos/products')
    stock=models.IntegerField()
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product_name
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])


#  class Store(models.Model):
#     name = models.CharField(max_length=100)
#     address = models.CharField(max_length=200)
#     phone = models.CharField(max_length=20)
#     email = models.EmailField()
#     website = models.URLField()
#     opening_hours = models.CharField(max_length=100)
#     rating = models.FloatField()
#     reviews = models.TextField()
#     products = models.ManyToManyField('Product', related_name='stores')
