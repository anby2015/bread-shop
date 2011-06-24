# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request, template_name="catalog/index.html"):
    page_title = 'Welcome | Order System'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))