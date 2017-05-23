from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import Birth_Stones, Premier_Brands, ClientQuery, ClientForm
# Create your views here.

def index(request):
    birthstones = Birth_Stones.objects.order_by('stone_month')
    premier_brands = Premier_Brands.objects.order_by('brand_name')
    return render(request, 'index.html', {'birthstones': birthstones, 'premier_brands': premier_brands})

def about(request):
    birthstones = Birth_Stones.objects.order_by('stone_month')
    premier_brands = Premier_Brands.objects.order_by('brand_name')
    return render(request, 'details/about.html', {'birthstones': birthstones, 'premier_brands': premier_brands})

def product(request):
    birthstones = Birth_Stones.objects.order_by('stone_month')
    premier_brands = Premier_Brands.objects.order_by('brand_name')
    return render(request, 'details/product.html', {'birthstones': birthstones, 'premier_brands': premier_brands})

def contact(request):
    birthstones = Birth_Stones.objects.order_by('stone_month')
    premier_brands = Premier_Brands.objects.order_by('brand_name')

    form = ClientForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():
            new_query = ClientQuery.objects.create(
                full_name = form.cleaned_data['full_name'],
                email_address = form.cleaned_data['email_address'],
                client_query = form.cleaned_data['client_query']
            )
            messages.success(request, 'Thank you for your query! We will contact you as soon as possible.')
            return HttpResponseRedirect('/contact/')
    else:
        form = ClientForm()
    return render(request, 'details/contact.html', {'birthstones': birthstones, 'premier_brands': premier_brands, 'form': form})    

def detail(request, premier_brand_name):
    birthstones = Birth_Stones.objects.order_by('stone_month')
    premier_brands = Premier_Brands.objects.order_by('brand_name')
    brand = get_object_or_404(Premier_Brands, pk=premier_brand_name)
    return render(request, 'brands/detail.html', {'brand': brand, 'birthstones': birthstones, 'premier_brands': premier_brands})


