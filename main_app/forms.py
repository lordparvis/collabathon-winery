from django.forms import ModelForm
from .models import Subscriber

class Subscriber_Form(ModelForm):
    class Meta:
        model = Subscriber


