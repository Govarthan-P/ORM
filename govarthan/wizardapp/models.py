from django.db import models
from django.contrib import admin
class service_DB(models.Model):
    Reg_No=models.IntegerField(primary_key=True,max_length=8)
    Name=models.CharField(max_length=10)
    Vehicle_no=models.CharField(max_length=7)
    DoR=models.DateField()
    Email=models.EmailField()
    Address=models.TextField()
    Mobile=models.IntegerField()
class service_DBAdmin(admin.ModelAdmin):
    list_display=["Reg_No","Name","Vehicle_no","Email","Address","Mobile"]