from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
class QueryView(TemplateView):
    template_name = "frontend/queries.html"