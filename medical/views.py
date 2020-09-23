from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,get_object_or_404
from background_task import background
from background_task.models import Task
from datetime import datetime
from django.core.mail import send_mail, EmailMessage
from django.template.loader import get_template
from django.utils import timezone   
from .models import *
import time
import requests
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


def regularPatientReports(request):
    patients = RegularPatient.objects.all()
    now = timezone.now()
    for patient in patients:

        delta = now - patient.purchase_date
        print(delta.days)

        if delta.days == 5:
            subject = 'Short Medicines'
            message = 'Medicines of Regular Customer: '+ patient.firstName + ' '+ patient.lastName + '\nMobile No: '+patient.mobile+ '\nMedicines:\n'+ patient.regularMedicines
            to = ['pratikkatariya01@gmail.com']
            
            # print(message)

            msg = EmailMessage(subject=subject, body=message, from_email='elitprojects01@gmail.com', to= to)

            try:
                # msg.send()
                print('Mail sent')
            except:
                pass    

        if delta.days == 3 and patient.alert:
            url = "https://www.fast2sms.com/dev/bulk"
            
            message = "\nDear "+patient.firstName+ ",\nYour regular medicines are available:\n"+patient.regularMedicines+"\nAanandkrupa Medical and General Stores"
            querystring = {"authorization":"m5tpoCJ7HbMVUOalGrzyk6qhscB8XfDYjA3dTZi4uL9IKFwWPSscIRojXrHY5PDOS6pNaqK0fAZUgBGV","sender_id":"FSTSMS","message": message,"language":"english","route":"p","numbers":patient.mobile}


            headers = {
            'cache-control': "no-cache"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            # print(response.text)
            print('SMS sent to customer that medicines are available')



    return HttpResponse("Hello world!")



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

def qrcodes(request, id):
    data = get_object_or_404(Product , product_id = id)
    

    # encode_data = data.product_name + ";M"+str(data.mrp)+";W"+str(data.wholesale_rate)+";Com"+data.company_name+";Ag "+data.agency_name+";Date"+str(data.purchase_date) 

    encode_data = data.product_name + " M "+str(data.mrp)+" W "+str(data.wholesale_rate)+" Com "+data.company_name

    ctx ={
       'data' : data,
       'encode_data': encode_data,
    }
    return render(request, 'qrcodes.html', ctx)