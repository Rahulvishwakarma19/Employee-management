from django.shortcuts import render,redirect
from .models import Emp,Testimonial
from django.http import HttpResponse


# Create your views here.
def emp_home(request):
    # return HttpResponse("Student home page")
    emps=Emp.objects.all()
    return render(request,"emp/home.html",{
        'emps':emps
    })

def add_emp(request):
    if request.method=="POST":
        #data fetch 
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")
        #create model object and set the data 
        e=Emp()
        e.name=emp_name
        e.e_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        #save the object 
        e.save()
        #prepare msg
        return redirect("/emp/home/")
    return render(request,"emp/add-emp.html",{})

def delete_emp(request,e_id):
    emp=Emp.objects.get(pk=e_id)
    emp.delete()
    return redirect("/emp/home/")

def update_emp(request,e_id):
    emp=Emp.objects.get(pk=e_id)
    return render(request, "emp/update_emp.html",{
        'emp':emp
    })
def do_update_emp(request,e_id):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        e=Emp.objects.get(pk=e_id)
        e.name=emp_name
        e.e_id=emp_id_temp 
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True

        e.save()
    return redirect("/emp/home/")

def testimonials(request):
    testi=Testimonial.objects.all()
    return render(request,"emp/testimonials.html",{
        'testi':testi
    })