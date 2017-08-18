import os
import requests
import json

from .models import *

# Facebook Feed from Graphs API

access_token = json.loads(requests.get(
    "https://graph.facebook.com/oauth/access_token?client_id=" + os.environ.get('CLIENT_ID') + "&client_secret=08f0ca27a2a4a5ee11e9a3552ad431e7&grant_type=client_credentials").content.decode('utf-8'))['access_token']

results = json.loads(requests.get(
    "https://graph.facebook.com/1476124115964835/feed?fields=permalink_url&limit=4&access_token=" + access_token).content.decode('utf-8'))['data']

facebook_feed = []

for post in results:
    facebook_feed.append(post["permalink_url"])

def add_variable_to_context(request):
    birthstones = Birth_Stones.objects.order_by('stone_month')
    premier_brands = Premier_Brands.objects.order_by('brand_name')
    new_arrivals = NewArrivals.objects.order_by('created_at')
    carousel_slides = CarouselSlides.objects.order_by('created_at')
    services = Services.objects.order_by('service_name')

    return {
        'birthstones': birthstones,
        'premier_brands': premier_brands,
        'services': services,
        'carousel_slides': carousel_slides,
        'new_arrivals': new_arrivals,
        'facebook_feed': facebook_feed,
    }