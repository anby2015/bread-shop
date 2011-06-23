from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "catalog_products"
        ordering = ['-created_at']

    def __unicode__(self):
            return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('catalog_product', (), {'product_slug': self.slug})


class Category(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    description = models.TextField()

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "catalog_categories"
        ordering = ['-created_at']

    def __unicode__(self):
            return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('catalog_category', (), {'category_slug': self.slug})
