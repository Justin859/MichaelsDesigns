from django import forms

class NewsletterForm(forms.Form):
    email = forms.EmailField(label='Your email', max_length=255)
    fname = forms.CharField(label='Your First Name', max_length=255)
    lname = forms.CharField(label='Your Last Name', max_length=255)