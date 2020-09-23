from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

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
    company_name = models.CharField(max_length=512, blank=True, null=True)
    mrp = models.FloatField() 
    wholesale_rate = models.FloatField() 
    margin = models.FloatField()
    agency_name = models.CharField(max_length=512, blank=True, null=True)
    purchase_date = models.DateField()
    qr_code = models.URLField(max_length=200, blank=True, null=True)

    # def __str__(self):
    #     return str(self.product_name)
    
    def save(self, *args, **kwargs): 
        string = ""
        
        if self.product_id:
            string = "https://project-shop.herokuapp.com/products/"+ str( self.product_id )
        else:
            list = Product.objects.last()
            string = "https://project-shop.herokuapp.com/products/"+ str( list.product_id + 1 )

        self.qr_code = string
        super(Product, self).save(*args, **kwargs) 
    
    # def save(self, *args, **kwargs):
    #     string = self.product_name + " "+ str(self.mrp) + str(self.wholesale_rate) 
    #     qrcode_img = qrcode.make(string)
    #     canvas = Image.new('RGB', (290, 290), 'white')
    #     draw = ImageDraw.Draw(canvas)
    #     canvas.paste(qrcode_img)
    #     fname = f'qrcode-{self.product_id}.png'
    #     buffer = BytesIO()
    #     canvas.save(buffer, 'PNG')
    #     self.qr_code.save(fname, File(buffer), save= False)
    #     canvas.close()
    #     super().save(*args, **kwargs)

