from django.http import HttpResponse
from django.shortcuts import render
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


def product_new(request, name="pomidor"):
    try:
        product = Product(name=name)
        product.save()
        return HttpResponse(f"<h3>id: {product.id} name: {product.name}</h3>")
    except Exception as e:
        return HttpResponse(f"<h1><b>{e}</b></h1>")


def product_list(request):
    out = Product.objects.all()
    outHtml = '<div>'

    for i in out:
        outHtml += "<h3>" + i.name + "</h3>" + "<br>"

    outHtml += '</div>'
    return HttpResponse(outHtml)
