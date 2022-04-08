from django.urls import path
from . import views

urlpatterns = [
    path(r'trigger-brand', views.load_brand_file, name='load_brand_file'),
    path(r'embed-token', views.EmbedToken.as_view(), name='embed-token')
]
