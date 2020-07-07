from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Subscriber
from .forms import Subscriber_Form


# Create your views here.

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    subscribers = Subscriber.objects.all()
    context = {'subscribers': subscribers}
    return render(request, 'admin.html', context)



#create & index subscriber form
def subscriber_index(request):
  if request.method == 'POST':
    subscriber_form = Subscriber_Form(request.POST)
    if subscriber_form.is_valid():
      subscriber_form.save()
  else:
    subscriber_form=Subscriber_Form()
  context = {'subscriber_form': subscriber_form}
  return render(request, 'home.html',context)

