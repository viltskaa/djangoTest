from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('product/add', views.product_new),
    path('product/edit/<id>', views.edit_product),
    path('product/delete/<id>', views.delete_product),
    path('product/delete_submit/<id>', views.delete_with_submit)
]
