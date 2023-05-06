from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ProductName
from .models import Product


def homePage(request):
    return HttpResponse('<h1>HOME</h1>')


def index(request):
    out = Product.objects.all()
    products = []

    for product in out:
        products.append((
            product.id,
            product.name
        ))

    return render(request, "productList.html", {'products': products})


def my_name(request, name: str):
    vowels = "aeiyou"

    name_to_data = []
    for letter in name:
        is_vowel = False
        if letter.lower() in vowels:
            is_vowel = True

        name_to_data.append(
            [letter, is_vowel]
        )

    data = {
        "word": name_to_data
    }
    return render(request, 'test.html', data)


def product_new(request):
    if request.method == "POST":
        try:
            form = ProductName(request.POST)
            if form.is_valid():
                name = form['product_name'].value()
                product = Product(name=name)
                product.save()
                return redirect("/")
        except Exception as e:
            form = ProductName(request.POST)
            return render(request, "addProduct.html", {
                'form': form,
                'error_message': "такое имя занято"
            })
    else:
        form = ProductName()
        return render(request, "addProduct.html", {'form': form})


def product_list(request):
    out = Product.objects.all()
    products = []

    for product in out:
        products.append((
            product.id,
            product.name
        ))

    return render(request, "productList.html", {'products': products})


def edit_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductName(request.POST)
        if form.is_valid():
            name = form['product_name'].value()
            product.name = name
            try:
                product.save()
                return redirect("/")
            except Exception as e:
                form = ProductName(request.POST)
                return render(request, "addProduct.html", {
                    'form': form,
                    'error_message': "такое имя занято"
                })
    else:
        form = ProductName(initial={
            "product_name": product.name
        })

        return render(request, "addProduct.html", {'form': form})


def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("/")


def delete_with_submit(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        product.delete()
        return redirect("/")
    else:
        return render(request,
                      "submitAction.html",
                      {'message': f"Вы точно хотите удалить продукт с id {product.id}, name {product.name}"})
