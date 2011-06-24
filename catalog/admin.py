from django.contrib import admin
from catalog.forms import ProductAdminForm
from catalog.models import Product, Category, ProductReview

__author__ = 'leroy'

class ProductAdmin(admin.ModelAdmin):

    form = ProductAdminForm

    list_display = ('name', 'price', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'description', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ('name', 'description',)
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'title', 'date', 'rating', 'is_approved')
    list_per_page = 20
    list_filter = ('product', 'user', 'is_approved')
    ordering = ['date']
    search_fields = ['user','content','title']

admin.site.register(ProductReview, ProductReviewAdmin)