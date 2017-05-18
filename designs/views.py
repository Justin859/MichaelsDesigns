from django.shortcuts import render
from django.http import HttpResponse

from .models import Birth_Stones
# Create your views here.
def index(request):
    birthstones = Birth_Stones.objects.order_by('stone_month')
    return render(request, 'index.html', {'birthstones': birthstones})




