from django.db import models


# Create your models here.
class account(models.Model):
    employ_id = models.CharField(max_length=10, primary_key=True)
    employ_name = models.CharField(max_length=10, null=True)
    employ_pwd = models.CharField(max_length=10, null=True)
