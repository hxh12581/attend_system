from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from leave.models import leave


# Create your views here.
def leave_message(request):
    employ_id = request.session.get('login_employ_id')
    employ_name = request.session.get('login_employ_name')
    messages = leave.objects.filter()
    return render(request, "leave/leave_message.html",
                  {"employ_id": employ_id, "employ_name": employ_name, "message": messages})


def leave_add_show(request):
    employ_id = request.session.get('login_employ_id')
    employ_name = request.session.get('login_employ_name')
    return render(request, 'leave/leave_add_show.html', {"employ_id": employ_id, "employ_name": employ_name})


def leave_add(request):
    if request.method == "POST":
        leave_id = request.POST.get('leave_id')
        leave_name = request.POST.get('leave_name')
        leave_status_reason = request.POST.get('leave_statu_reason')
        leave_reason = request.POST.get('leave_reason')
        leave_stime = request.POST.get('leave_stime')
        leave_etime = request.POST.get('leave_etime')
        leave.objects.create(leave_id=leave_id, leave_name=leave_name, leave_statu_reason=leave_status_reason,
                             leave_statu='已请假', leave_reason=leave_reason, leave_stime=leave_stime,
                             leave_etime=leave_etime)
    return redirect('leave_message')


def leave_update_show(request, id):
    employ_id = request.session.get('login_employ_id')
    employ_name = request.session.get('login_employ_name')
    update_messages = leave.objects.filter(id=id).first()
    return render(request, 'leave/leave_update_show.html',
                  {"employ_id": employ_id, "employ_name": employ_name, "update_messages": update_messages,
                   "id": update_messages.id})


def leave_update(request,id):
    if request.method == "POST":
        leave_id = request.POST.get('leave_id')
        leave_name = request.POST.get('leave_name')
        leave_status_reason = request.POST.get('leave_statu_reason')
        leave_reason = request.POST.get('leave_reason')
        leave_stime = request.POST.get('leave_stime')
        leave_etime = request.POST.get('leave_etime')
        try:
            update_id = leave.objects.get(id=id)
            update_id.leave_id = leave_id
            update_id.leave_name = leave_name
            update_id.leave_statu_reason = leave_status_reason
            update_id.leave_reason = leave_reason
            update_id.leave_stime = leave_stime
            update_id.leave_etime = leave_etime
            update_id.save()
            return redirect('leave_message')
        except leave.DoesNotExist:
            return HttpResponse("指定的序号不存在")


def leave_pop(request,id):
    leave.objects.get(id=id).delete()
    return redirect('leave_message')
