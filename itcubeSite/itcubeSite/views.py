from django.http import HttpResponse
from django.shortcuts import render

from .forms import ProductName
from .models import Product


def homePage(request):
    return HttpResponse('<h1>HOME</h1>')


def index(request):
    return render(request, 'index.html')


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
            if request.method == "POST":
                form = ProductName(request.POST)
                if form.is_valid():
                    name = form['product_name'].value()
                    product = Product(name=name)
                    product.save()
                    return HttpResponse(f"<h3>id: {product.id} name: {product.name}</h3>")
        except Exception as e:
            return HttpResponse(f"<h1><b>Продукт с этим именем уже есть!</b>{e}</h1>")
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
