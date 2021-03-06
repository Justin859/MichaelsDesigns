import mailchimp
import sys

sys.path.append('./gettingstarted/')

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from .forms import NewsletterForm
from .models import Birth_Stones, Premier_Brands, ClientQuery, ClientForm, NewArrivals
from gettingstarted import secret_keys
from secret_keys import *
import json
import requests
import os

# Create your views here.

def index(request):
    new_arrivals = NewArrivals.objects.order_by('created_at')

    access_token = json.loads(requests.get(
        "https://graph.facebook.com/oauth/access_token?client_id=" + os.environ.get('CLIENT_ID') + "&client_secret=" + os.environ.get('FB_APP_SECRET')  + "&grant_type=client_credentials").content.decode('utf-8'))['access_token']

    results = json.loads(requests.get(
        "https://graph.facebook.com/1476124115964835/feed?fields=permalink_url&limit=4&access_token=" + access_token).content.decode('utf-8'))['data']

    facebook_feed = []

    for post in results:
        facebook_feed.append(post["permalink_url"])

    return render(request, 'index.html', {'new_arrivals': new_arrivals, 'facebook_feed': facebook_feed})

def about(request):

    return render(request, 'details/about.html')

def product(request):

    return render(request, 'details/product.html')

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
            full_name = form.cleaned_data['full_name']
            email_address = form.cleaned_data['email_address']
            client_query = form.cleaned_data['client_query']
            try:
                send_mail('Online Query', 'email: ' + email_address + '\n\nclient name: ' + full_name + '\n\nclient query: \n\n' + client_query, 'queries@michaelsdesigns.co.za', ['corne@michaelsdesigns.co.za'])
            except BadHeaderError:
                return HttpResponse('Invalid Header found.')

            messages.success(request, 'Thank you for your query! We will contact you as soon as possible.')
            return HttpResponseRedirect('/')
    else:
        form = ClientForm()
    return render(request, 'details/contact.html', {'form': form})    

def newsletter_signup(request):
    birthstones = Birth_Stones.objects.order_by('stone_month')
    premier_brands = Premier_Brands.objects.order_by('brand_name')

    if request.method == 'POST':

        form = NewsletterForm(request.POST)

        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            email = form.cleaned_data['email']

            try:
                API_KEY = SECRET_API_KEY
                LIST_KEY = SECRET_LIST_KEY

                api = mailchimp.Mailchimp(API_KEY)
                api.lists.subscribe(LIST_KEY, {'email': email}, merge_vars={'FNAME':fname,'LNAME':lname})
            except BadHeaderError:
                return HttpResponse('Invalid Header found')
                
            messages.success(request, 'Thank you for signing up to our newsletter! An email was sent to you for confirmation.')
            return HttpResponseRedirect('/')
    else:
        form = NewsletterForm()
    return render(request, 'newsletter_signup.html', {'birthstones': birthstones, 'premier_brands': premier_brands, 'form': form})

def detail(request, premier_brand_name):
    brand = get_object_or_404(Premier_Brands, pk=premier_brand_name)
    return render(request, 'brands/detail.html', {'brand': brand})

def services(request):

    return render(request, 'repairs/services.html')

def anniversary(request):
    
    return render(request, 'anniversary.html')