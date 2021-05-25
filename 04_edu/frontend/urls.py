from django.urls import path

from .views import QueryView

app_name = 'frontend'

urlpatterns = [
    path('', QueryView.as_view(), name='query'),
]
