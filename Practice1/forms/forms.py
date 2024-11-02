from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='Your name',max_length=100)
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(label='Message', widget=forms.Textarea)