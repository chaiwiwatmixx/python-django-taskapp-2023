from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def register(request):
    #ส่งข้อมูลจากฟอร์ม
    if request.method == "POST":
        #รับค่า
        username = request.POST["username"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        #ตรวจสอบว่าเป็นค่าว่างหรือไม่
        if username == "" or password == "" or repassword == "":
            messages.warning(request, "กรุณาป้อนข้อมูลให้ครบ")
            return redirect("/register")
        else:
            #รหัสผ่านตรงกันหรือไม่
            if password == repassword:
                return redirect("/login")
            else:
                messages.warning(request, "รหัสผ่านไม่ตรงกัน")
                return redirect("/register")
    else:
        return render(request, "register.html")
    

def login(request):
    return render(request, "login.html")
