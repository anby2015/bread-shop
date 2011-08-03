from django.conf.urls.defaults import patterns
from django.template.defaulttags import url

__author__ = 'leroy'

urlpatterns = patterns('catalog.views',
    (r'^$','index', {'template_name': 'catalog/index.html'}, 'catalog_home'),
    (r'^product/$', 'product', {'template_name': 'catalog/product.html'}, 'catalog_product'),
    (r'^promotion/$', 'promotion', {'template_name': 'catalog/promotion.html'}, 'catalog_promotion'),
    (r'^about/$', 'about', {'template_name': 'catalog/about.html'}, 'catalog_about'),
#    (r'^category/(?P<category_slug>[-\w]+)/$', 'show_category',
#       {'template_name': 'catalog/category.html'}, 'catalog_category'),
#    (r'^product/(?P<product_slug>[-\w]+)/$', 'show_product',
#       {'template_name': 'catalog/product.html'}, 'catalog_product'),
#    (r'^tag_cloud/$', 'tag_cloud',
#       {'template_name': 'catalog/tag_cloud.html'}, 'tag_cloud'),
#    (r'^tag/(?P<tag>[-\w]+)/$', 'tag',
#       {'template_name': 'catalog/tag.html'}, 'tag'),
#    (r'^review/product/add/$', 'add_review', {}, 'add_product_review'),
#    (r'^tag/product/add/$', 'add_tag'),
)
  