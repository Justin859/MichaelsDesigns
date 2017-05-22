from django.db import models
from django.utils.timezone import datetime

from django.forms import ModelForm
# Create your models here.

class Birth_Stones(models.Model):

    MONTH_CHOICES=((1, "January"), (2, "February"), (3, "March"),
                   (4, "April"), (5, "May"), (6, "June"),
                   (7, "July"), (8, "August"), (9, "September"),
                   (10, "October"), (11, "November"), (12, "December"))
    
    stone_name = models.CharField(max_length=255, primary_key=True)
    stone_month = models.IntegerField(choices=MONTH_CHOICES)
    stone_photo = models.ImageField(upload_to=('designs/static/images/birth_stones'), max_length=255, null=True)
    description = models.TextField()
    cleaning_tips = models.TextField()

    class Meta:
        verbose_name = 'Birth Stone'
        verbose_name_plural = 'Birth Stones'

    def __str__(self):
        return self.stone_name

class Premier_Brands(models.Model):

    brand_name = models.CharField(max_length=255, primary_key=True)
    brand_main_photo = models.ImageField(upload_to='designs/static/images/premier_brands/brand_main_photo', max_length=255, null=True)
    brand_logo = models.ImageField(upload_to='designs/static/images/premier_brands/brand_logo', max_length=255, null=True)
    brand_description = models.TextField()
    

    class Meta:
        verbose_name = 'Premier Brand'
        verbose_name_plural = 'Premier Brands'

    def __str__(self):
        return self.brand_name

class ClientQuery(models.Model):
    
    full_name = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255)
    client_query = models.TextField(max_length=1001)
    sent_at = models.DateField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = 'Client Query'
        verbose_name_plural = 'Client Queries'

    def __str__(self):
        return str(self.sent_at) + " : " + self.email_address

class ClientForm(ModelForm):
    class Meta:
        model = ClientQuery
        fields = ['full_name', 'email_address', 'client_query']

