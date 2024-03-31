from django.http import HttpResponse
from django.shortcuts import render, redirect

from account import models
from account.models import account
from employ_message.models import employee


# Create your views here.

def employ_message(request):
    employ_id = request.session.get('login_employ_id')
    employ_name = request.session.get('login_employ_name')
    messages = employee.objects.filter(employ_id=employ_id)
    return render(request, "employee/employ_message.html",
                  {"employ_id": employ_id, "employ_name": employ_name, "message": messages})


def employ_message_update(request):
    employ_id = request.session.get('login_employ_id')
    employ_name = request.session.get('login_employ_name')
    return render(request, 'employee/employ_message_update.html', {"employ_id": employ_id, "employ_name": employ_name})


def employ_message_insert(request):
    if request.method == 'POST':
        employ_id = request.session.get('login_employ_id')
        employ_name = request.session.get('login_employ_name')
        employ_age = request.POST.get("employ_age")
        employ_gender = request.POST.get("employ_gender")
        employ_Phone = request.POST.get("employ_Phone")
        try:
            emp_record = employee.objects.get(employ_id=employ_id, employ_name=employ_name)
            emp_record.employ_age = employ_age
            emp_record.employ_gender = employ_gender
            emp_record.employ_Phone = employ_Phone
            emp_record.save()
            return redirect('employ_message')
        except employee.DoesNotExist:
            return HttpResponse("指定的员工信息不存在")


def employ_message_cancel(request):
    employ_id = request.session.get('login_employ_id')
    employee.objects.get(employ_id=employ_id).delete()
    account.objects.get(employ_id=employ_id).delete()
    return redirect('login')
