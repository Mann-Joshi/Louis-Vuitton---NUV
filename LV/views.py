from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Product

class LV(TemplateView):
    template_name="homepage.html"

class men(TemplateView):
    template_name="men.html"

class women(TemplateView):
    template_name="women.html"

class category(ListView):
    model = Product
    template_name='homepage.html'
    context_object_name = 'data'
