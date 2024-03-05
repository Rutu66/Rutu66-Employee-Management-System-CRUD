from django.db import models

# Create your models here.

class employee(models.Model):
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    salary = models.IntegerField(null=True,)
    join_date = models.DateTimeField(auto_now_add=True)
    
