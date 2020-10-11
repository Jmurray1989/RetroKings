from django.db import models
from django.contrib.auth.models import User

# Categories Model


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Products Model


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6,
                                 decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Model to define the fields required to add a review to a product
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                null=True, blank=True, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True,
                             related_name="reviews")
    comment = models.TextField(max_length=1000,
                               blank=True)
    rating = models.IntegerField(default=1)

    def __str__(self):
        return self.user.username
