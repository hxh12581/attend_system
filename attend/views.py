from django.shortcuts import render, redirect
from attend.models import attend
from account.models import account


# Create your views here.

def attend_message(request):
    employ_id = request.session.get('login_employ_id')
    employ_name = request.session.get('login_employ_name')
    messages = attend.objects.filter(attend_id=employ_id)
    return render(request, "attend/attend_message.html",
                  {"employ_id": employ_id, "employ_name": employ_name, "message": messages})


def attend_sgin_in(request):
    employ_id = request.session.get('login_employ_id')
    employ_name = request.session.get('login_employ_name')
    return render(request, 'attend/attend_sgin_in.html', {"employ_id": employ_id, "employ_name": employ_name})


def attend_sign_out(request):
    employ_id = request.session.get('login_employ_id')
    employ_name = request.session.get('login_employ_name')
    return render(request, 'attend/attend_sign_out.html', {"employ_id": employ_id, "employ_name": employ_name})


def sgin(request):
    attend_id = request.session.get('login_employ_id')
    attend_name = request.session.get('login_employ_name')
    if request.method == "POST":
        attend_stime = request.POST.get('sign_in')
        attend.objects.create(attend_id=attend_id, attend_name=attend_name, attend_statu='已签到',
                              attend_stime=attend_stime)
    return redirect('attend_message')


def out(request):
    attend_id = request.session.get('login_employ_id')
    attend_name = request.session.get('login_employ_name')
    if request.method == "POST":
        attend_etime = request.POST.get('sign_out')
        attend.objects.create(attend_id=attend_id, attend_name=attend_name, attend_statu='已签退',
                              attend_etime=attend_etime)
    return redirect('attend_message')
