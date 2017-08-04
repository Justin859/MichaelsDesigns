import requests
import json

from .models import *

# Facebook Feed from Graphs API
access_token = json.loads(requests.get(
    "https://graph.facebook.com/oauth/access_token?client_id=893940824090857&client_secret=08f0ca27a2a4a5ee11e9a3552ad431e7&grant_type=client_credentials").content)['access_token']

results = json.loads(requests.get(
    "https://graph.facebook.com/1476124115964835/feed?fields=permalink_url&limit=4&access_token=" + access_token).content)['data']

facebook_feed = []

for post in results:
    facebook_feed.append(post["permalink_url"])

def add_variable_to_context(request):
    birthstones = Birth_Stones.objects.order_by('stone_month')
    premier_brands = Premier_Brands.objects.order_by('brand_name')

    return {
        'birthstones': birthstones,
        'premier_brands': premier_brands,
        'facebook_feed': facebook_feed,
    }