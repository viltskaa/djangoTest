from django.db import models


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,
                            null=False,
                            unique=True)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,
                            null=False,
                            unique=True)


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now=True)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.SET_NULL,
                                 null=True
                                 )
    products = models.ManyToManyField(Product, symmetrical=True)


class Shipments(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
