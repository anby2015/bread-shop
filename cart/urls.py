__author__ = 'leroy'

from django.conf.urls.defaults import *

urlpatterns = patterns('bread.cart.views',
    (r'^$', 'show_cart', {'template_name':'cart/cart.html'}, 'show_cart'),
)
