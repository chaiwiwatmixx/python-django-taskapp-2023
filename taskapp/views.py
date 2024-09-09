from django.shortcuts import render, redirect
from django.http import HttpResponse
from taskapp.models import Task
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    if request.method == "POST":
        #ดึงข้อมูลจากฟอร์ม
        name = request.POST["name"]
        #เช็คค่าว่าง
        if name == "":
            #ส่งข้อความแจ้งเตือนผู้ใช้
            messages.warning(request, "กรุณาป้อนชื่อรายการ")
            return redirect("/")
        else:
            #บันทึกข้อมูล
            task = Task.objects.create(name = name)
            task.save()
            messages.success(request, "บันทึกข้อมูลเรียบร้อย")
            return redirect("/")
    else:
        all_task = Task.objects.all()
        #
        page = request.GET.get("page")
        paginator = Paginator(all_task, 5)
        all_task = paginator.get_page(page)
        return render(request,"index.html",{"all_task":all_task})
    
def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.status=True
    task.save()
    messages.success(request, "เปลี่ยนสถาณะเรียบร้อย")
    return redirect("/")

def pending_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.status=False
    task.save()
    messages.success(request, "เปลี่ยนสถาณะเรียบร้อย")
    return redirect("/")