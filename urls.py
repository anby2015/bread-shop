from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('bread.catalog.views',
    # Examples:
    url(r'^', include('bread.catalog.urls')),
    url(r'^cart/', include('bread.cart.urls')),
    #url(r'^$', 'bread.views.home', name='home'),
    #url(r'^bread/', include('bread.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
