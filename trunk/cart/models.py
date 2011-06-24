from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from catalog.models import Product

class CartItem(models.Model):
    
    """ model class containing information each Product instance in the customer's shopping cart """
    cart_id = models.CharField(max_length=50, db_index=True)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Product, unique=False)

    class Meta:
        db_table = 'cart_items'
        ordering = ['date_added']

    @property
    def total(self):
        return self.quantity * self.product.price

    @property
    def name(self):
        return self.product.name

    @property
    def price(self):
        return self.product.price

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def argument_quantity(self, quantity):
        """ called when a POST request comes in for a Product instance already in the shopping cart """
        self.quantity = self.quantity + int(quantity)
        self.save()


class UserPredefinedCart(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for product page URL, created automatically from name.')

    description = models.TextField()
    is_default = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, null=True)

    class Meta:
        db_table = 'cart_user_predefined_cart'
        ordering = ['-created_at', 'user']
        verbose_name_plural = 'User Predefined Shopping Cart'

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('cart_user_defined', (), { 'product_slug': self.slug })


class UserPreSelectCartItem(models.Model):

    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Product, unique=False)

    cart = models.ForeignKey(UserPredefinedCart, null=False)
