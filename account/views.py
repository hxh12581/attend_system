from django.shortcuts import render, redirect

from account import models
from employ_message.models import employee
from attend.models import attend
from leave.models import leave


def login(request):
    if request.method == 'POST':
        employ_id = request.POST.get('employ_id')
        employ_name = request.POST.get('employ_name')
        employ_pwd = request.POST.get('employ_pwd')
        account = models.account.objects.filter(employ_id=employ_id).first()
        if account and account.employ_pwd == employ_pwd and account.employ_name == employ_name:
            request.session["login_employ_id"] = account.employ_id
            request.session["login_employ_name"] = account.employ_name
            return redirect('employ_message')
        else:
            return render(request, "account/login.html", {"error_msg": "员工号或密码错误"})
    return render(request, "account/login.html")


def regist(request):
    if request.method == "POST":
        employ_id = request.POST.get('employ_id')
        employ_name = request.POST.get('employ_name')
        employ_pwd = request.POST.get('employ_pwd')
        existing_account = models.account.objects.filter(employ_id=employ_id)
        if existing_account.exists():
            return render(request, 'account/regist.html', {"error_msg": "员工号已存在"})
        else:
            models.account.objects.create(employ_id=employ_id, employ_name=employ_name, employ_pwd=employ_pwd)
            employee.objects.create(employ_id=employ_id, employ_name=employ_name)
            return render(request, 'account/regist.html', {"success_msg": "注册成功"})
    return render(request, "account/regist.html")


def index(request):
    return render(request, "index.html")


def loginout(request):
    if request.session.get("login_employ_name"):
        del request.session["login_employ_name"]
    return render(request, 'account/login.html')
