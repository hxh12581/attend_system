from django.db import models


# Create your models here.
class attend(models.Model):
    attend_id = models.CharField(max_length=10, null=True)
    attend_name = models.CharField(max_length=10, null=True)
    statu_choices = (
        ('已签到', 'Option 1'),
        ('已签退', 'Option 2'),
    )
    attend_statu = models.CharField(max_length=10, choices=statu_choices, null=True)
    attend_stime = models.DateTimeField(null=True)
    attend_etime = models.DateTimeField(null=True)

