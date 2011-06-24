from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    description = models.TextField()
    is_active = models.BooleanField(default=True)

    meta_keywords = models.CharField(max_length=255, help_text='Comma-delimited set of SEO keywords for keywords meta tag')
    meta_description = models.CharField(max_length=255, help_text='Content for description meta tag')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "catalog_categories"
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
            return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('catalog_category', (), {'category_slug': self.slug})

class Product(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    sku = models.CharField(max_length=50)

    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()

    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    meta_keywords = models.CharField("Meta Keywords",max_length=255, help_text='Comma-delimited set of SEO keywords for keywords meta tag')
    meta_description = models.CharField("Meta Description", max_length=255, help_text='Content for description meta tag')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = "catalog_products"
        ordering = ['-created_at']

    def __unicode__(self):
            return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('catalog_product', (), {'product_slug': self.slug})


class ProductReview(models.Model):

    """ model class containing product review data associated with a product instance """
    RATINGS = ((5,5),(4,4),(3,3),(2,2),(1,1),)

    product = models.ForeignKey(Product)
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(default=5, choices=RATINGS)
    is_approved = models.BooleanField(default=True)
    content = models.TextField()

    class Meta:
        db_table = "catalog_product_reviews"
        ordering = ['-date']
        verbose_name_plural = 'Product Reviews'