from .models import *

def add_variable_to_context(request):
    birthstones = Birth_Stones.objects.order_by('stone_month')
    premier_brands = Premier_Brands.objects.order_by('brand_name')

    return {
        'birthstones': birthstones,
        'premier_brands' : premier_brands,
    }