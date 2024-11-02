from django import forms
from .models import Tweet

class Tweetform(forms):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']