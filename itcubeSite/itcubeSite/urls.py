from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/<name>', views.product_new),
    path('products', views.product_list),
    path('name/<name>', views.my_name),
    path('product/<id>')
]
