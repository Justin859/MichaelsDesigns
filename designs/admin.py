from django.contrib import admin
from designs.models import Birth_Stones, Premier_Brands, ClientQuery, NewArrivals, CarouselSlides
from django import forms
# Register your models here.

class CarouselSlidesForm(forms.ModelForm):
    class Meta:
        model = CarouselSlides
        fields = ('slide_name', 'slide_image', 'slide_for', 'first_slide')
        
    def clean(self):

        slide_init = self.cleaned_data.get('slide_for')
        is_first = self.cleaned_data.get('first_slide')
        name = self.cleaned_data.get('slide_name')
        carousel_slides = CarouselSlides.objects.filter(slide_for=slide_init)

        if not self.instance.id:
            for slide in carousel_slides:
                if slide.first_slide and is_first:
                    raise forms.ValidationError("There must not be more than one first slide. " + slide.slide_name + " is already the first slide for " + slide.slide_for)
                if slide.slide_name == name:
                    raise forms.ValidationError("'" + slide.slide_name + "' already exists in '" + slide.slide_for + "'")
        else:
            for slide in carousel_slides:
                if slide.slide_name == name and self.instance.id != slide.id:
                    raise forms.ValidationError("'" + slide.slide_name + "' already exists in '" + slide.slide_for + "'")
                if slide.first_slide and is_first and self.instance.id != slide.id:
                    raise forms.ValidationError("There must not be more than one first slide. " + slide.slide_name + " is already the first slide for " + slide.slide_for)

        return self.cleaned_data

class CarouselSlidesAdmin(admin.ModelAdmin):
    form = CarouselSlidesForm
    fields = ('slide_name', 'slide_image', 'slide_for', 'first_slide')


admin.site.register(Birth_Stones)
admin.site.register(Premier_Brands)
admin.site.register(ClientQuery)
admin.site.register(NewArrivals)
admin.site.register(CarouselSlides, CarouselSlidesAdmin)