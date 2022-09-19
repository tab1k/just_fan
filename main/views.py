from django.shortcuts import render
from .models import *
from products.models import *


# Create your views here.

def index(request):
    women_list = Women.objects.all()
    products = Product.objects.all()
    return render(request, 'main/index.html', {'women_list': women_list, 'products' : products})


def about(request):
    return render(request, 'main/about.html')
