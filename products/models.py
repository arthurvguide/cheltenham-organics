"""
products/models.py: Contains the models Category, Product and Review.

Category and Product  was Inspired by Code Institute's Boutique Ado project,
but adapted to my project
Review is an "original model".
"""

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Model for loged-in customers review the products
    """
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=25,
                             null=False, blank=False)
    review_subject = models.TextField(max_length=250, null=False,
                                      blank=False)
    date_created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.title
