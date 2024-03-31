from django.db import models


# Create your models here.
class employee(models.Model):
    employ_id = models.CharField(max_length=10, primary_key=True)
    employ_name = models.CharField(max_length=10, null=True)
    employ_age = models.IntegerField(null=True)
    employ_gender = models.CharField(max_length=255, null=True)
    employ_Phone = models.CharField(max_length=11, null=True)