import os
import requests
import json

from .models import *

# Facebook Feed from Graphs API

def add_variable_to_context(request):
    birthstones = Birth_Stones.objects.order_by('stone_month')
    premier_brands = Premier_Brands.objects.order_by('brand_name')
    carousel_slides = CarouselSlides.objects.order_by('created_at')
    services = Services.objects.order_by('service_name')

    return {
        'birthstones': birthstones,
        'premier_brands': premier_brands,
        'services': services,
        'carousel_slides': carousel_slides,
    }