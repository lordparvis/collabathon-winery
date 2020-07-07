from django.forms import ModelForm
from .models import Subscriber
#from django import forms

class Subscriber_Form(ModelForm):
    class Meta:
        model = Subscriber
        fields = ['first_name','last_name','email']
