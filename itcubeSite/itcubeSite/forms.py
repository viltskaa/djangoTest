from django import forms
from .models import Customer, Product


class ProductName(forms.Form):
    product_name = forms.CharField(label="Product name", max_length=20)


class OrderNew(forms.Form):
    date = forms.DateField()
    customer = forms.ModelChoiceField(widget=forms.Select,
                                      queryset=Customer.objects.all())
    products = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                              queryset=Product.objects.all(),
                                              to_field_name="")
