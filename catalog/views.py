# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request, template_name="catalog/index.html"):
    page_title = 'Welcome | Order System'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def product(request, template_name="catalog/product.html"):
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def promotion(request, template_name="catalog/promotion.html"):
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def about(request, template_name="catalog/about.html"):
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))