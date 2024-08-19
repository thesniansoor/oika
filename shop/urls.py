from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),     
   # path("index", views.home),
    path("product_list", views.product_list),
]