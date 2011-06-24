from django.contrib import admin
from bread.cart.models import UserPreSelectCartItem, UserPredefinedCart

__author__ = 'leroy'

class UserPreSelectCartItemInline(admin.StackedInline):
    model = UserPreSelectCartItem
    extra = 0

class UserPredefineCartAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'user', 'created_at','updated_at','is_default')
    list_filter = ('user','is_default')
    list_per_page = 20
    ordering = ['user', '-created_at']
    search_fields = ('user',)
    inlines = [UserPreSelectCartItemInline,]
    prepopulated_fields = {'slug' : ('name',)}


admin.site.register(UserPredefinedCart, UserPredefineCartAdmin)