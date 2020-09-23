from django.contrib import admin
from .models import *

# Register your models here.

class TestAdmin(admin.ModelAdmin):
    list_display = ('row_id', 'message', 'time_now') 
    list_filter = ('time_now',)
    search_fields = ('row_id',)

class RegularPatientAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'gender', 'mobile', 'time_now', 'purchase_date') 
    list_filter = ('time_now', 'gender', 'purchase_date')
    search_fields = ('firstName', 'lastName', 'mobile', )

class WhatsappCustomerAdmin(admin.ModelAdmin):
    list_display = ('cus_id', 'firstName', 'lastName', 'gender', 'mobile','email', 'birthdate') 
    list_filter = ('gender',)
    search_fields = ('firstName', 'lastName', 'mobile', )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'company_name', 'mrp', 'wholesale_rate','margin', 'agency_name', 'purchase_date') 
    list_filter = ('company_name','agency_name', 'purchase_date')
    search_fields = ('product_name', 'company_name', 'mrp', 'agency_name')

admin.site.register(Message)
admin.site.register(Test, TestAdmin)
admin.site.register(RegularPatient, RegularPatientAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.register(WhatsappCustomer, WhatsappCustomerAdmin)