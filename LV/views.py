from django.http import HttpResponse
from django.views.generic import TemplateView

class LV(TemplateView):
    template_name="homepage.html"