from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('product_search.html', views.product_search, name='product_search'),
]