from django.urls import path

from . import views

urlpatterns = [
    path(r'trigger-brand', views.load_brand_file, name='load_brand_file'),
]
