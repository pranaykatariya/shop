from django.db import models

# Create your models here.
class Test(models.Model):
    row_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=64)
    time_now = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(null=False)
    message = models.TextField(null=True, blank=True)


class WhatsappCustomer(models.Model):
    cus_id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64   )
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=64) 

class RegularPatient(models.Model):
    # Compulsory
    patient_id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64,null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=64,null=True, blank=True)
    occupation = models.CharField(max_length=250,null=True, blank=True)
    
    # Comma seperated medicines 
    regularMedicines = models.TextField()
    
    # Functional
    repeat_schedule = models.IntegerField()
    alert = models.BooleanField(default=False, blank=True, null=True)
    time_now = models.DateTimeField(auto_now_add=True)
    purchase_date = models.DateTimeField()


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=512)
    company_name = models.CharField(max_length=512)
    mrp = models.IntegerField() 
    wholesale = models.IntegerField() 
    margin = models.FloatField()
    agency_name = models.CharField(max_length=512)
    purchase_date = models.DateTimeField()