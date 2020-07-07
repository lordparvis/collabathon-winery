from django.shortcuts import render

from django.http import HttpResponse

from .models import Subscriber


# Create your views here.

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    subscribers = Subscriber.objects.all()
    context = {'subscribers': subscribers}
    return render(request, 'admin.html', context)