from django import forms


class ProductName(forms.Form):
    product_name = forms.CharField(label="Product name", max_length=20)
