from django.http import HttpResponse
from django.views.generic import TemplateView

class LV(TemplateView):
    template_name="homepage.html"

class men(TemplateView):
    template_name="men.html"

class women(TemplateView):
    template_name="women.html"
