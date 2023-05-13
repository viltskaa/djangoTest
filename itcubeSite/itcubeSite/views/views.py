from django.http import HttpResponse
from django.shortcuts import render, redirect

from itcubeSite.itcubeSite.forms import ProductName
from itcubeSite.itcubeSite.models import Product


def homePage(request):
    return HttpResponse('<h1>HOME</h1>')


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
