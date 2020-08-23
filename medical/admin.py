from django.contrib import admin
from .models import *

# Register your models here.

class TestAdmin(admin.ModelAdmin):
    list_display = ('row_id', 'message', 'time_now') 
    list_filter = ('time_now',)
    search_fields = ('row_id',)


admin.site.register(Message)
admin.site.register(Test, TestAdmin)
admin.site.register(RegularPatient)