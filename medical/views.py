from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from background_task import background
from background_task.models import Task
from .models import *
import time
# Create your views here.

@background(schedule=0)
def hello():
    test = Test(message='a')
    test.save()
    print("Hello World!")
    print(str(time.time()))

def background_view(request):
    test = Test(message='a')
    test.save()
    return HttpResponse("Hello world !")


def home(request):
    return render(request, 'index.html')


def shop(request):
    return render(request, 'shop.html')


def about(request):
    return render(request, 'about.html')


def cart(request):
    return render(request, 'cart.html') 


def checkout(request):
    return render(request, 'checkout.html') 


def contact(request):
    return render(request, 'contact.html') 


def product(request):
    return render(request, 'shop-single.html') 


def thankyou(request):
    return render(request, 'thankyou.html') 


def regPatients(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'regularpatient.html') 