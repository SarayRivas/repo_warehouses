from django.db import models
from django.contrib.auth.models import User



      
class Warehouse(models.Model):
    id_warehouse = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
