from django.views.generic import DetailView, ListView
from django.shortcuts import render

from .models import Course

# Create your views here.
class CourseListView(ListView):
    model = Course
    page_name = 'курсы'


class CourseDetailView(DetailView):
    model = Course
    page_name = 'публикация'