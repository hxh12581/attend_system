from django.db import models


# Create your models here.

class leave(models.Model):
    leave_id = models.CharField(max_length=10, null=True)
    leave_name = models.CharField(max_length=10, null=True)

    statu_choices = (('因私请假', 'Option 1'), ('因公请假', 'Option 2'))
    leave_statu_reason = models.CharField(choices=statu_choices, null=True, max_length=10)

    statu_choices1 = (('已请假', 'Option 1'), ('已销假', 'Option 2'))
    leave_statu = models.CharField(choices=statu_choices1, null=True, max_length=10)
    leave_reason = models.CharField(max_length=255, null=True)
    leave_stime = models.DateTimeField(null=True)
    leave_etime = models.DateTimeField(null=True)
