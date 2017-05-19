from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Birth_Stones, Premier_Brands
# Create your views here.

#Global Variables
birthstones = Birth_Stones.objects.order_by('stone_month')
premier_brands = Premier_Brands.objects.order_by('brand_name')


def index(request):
    return render(request, 'index.html', {'birthstones': birthstones, 'premier_brands': premier_brands})

def about(request):
    return render(request, 'details/about.html', {'birthstones': birthstones, 'premier_brands': premier_brands})

def contact(request):
    return render(request, 'details/contact.html', {'birthstones': birthstones, 'premier_brands': premier_brands})    

def detail(request, premier_brand_name):
    brand = get_object_or_404(Premier_Brands, pk=premier_brand_name)
    return render(request, 'brands/detail.html', {'brand': brand, 'birthstones': birthstones, 'premier_brands': premier_brands})


