"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from background_task.models import Task

from medical.views import * 

urlpatterns = [

    path('', home, name='home'),
    path('background', background_view, name='background_view'),
    path('check', regularPatientReports, name='regularPatientReports'),
    path('shop', shop, name='shop'),
    path('about', about, name='about'),
    path('cart', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
    path('contact', contact, name='contact'),
    path('product', product, name='product'),
    path('thankyou', thankyou, name='thankyou'),

    path('regularpatients', regPatients, name='regPatients'),


    path('admin/', admin.site.urls),
]


hello(repeat= 60 ,repeat_until=None, priority = 8)