from django.urls import path
from .views import product_view, order_view

urlpatterns = [
    path('product', product_view.product_list),
    path('product/add', product_view.add_product),
    path('product/edit/<id>', product_view.edit_product),
    path('product/delete/<id>', product_view.delete_product),
    path('product/delete_submit/<id>', product_view.delete_with_submit),
    #
    path('order', order_view.list_order),
    path('order/add', order_view.new_order),
]
