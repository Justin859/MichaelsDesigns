from django.db import models

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

