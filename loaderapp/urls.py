from django.urls import path
from . import views

urlpatterns = [
    path(r'trigger-brand', views.LoadBrandFile.as_view(), name='load_brand_file'),

]
