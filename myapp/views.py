# from django.http import HttpResponse
import datetime
from django.shortcuts import render

def home(request):
    isActive=True
    if request.method=='POST':
        check=request.POST.get("check")
        if check is None: isActive=False
        else: isActive=True

    date=datetime.datetime.now()
    
    name="Learn code"
    list_of_subject=[
        "python",
        "java",
        "sql",
        "django",
        "spring"
    ]
    student={
        'student_name':"Rahul",
        'student_college':"Tolani",
        'student_city':"mumbai"
    }
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_subject':list_of_subject,
        'student_data':student
    }
    # print("Teest function is called from view")
    # return HttpResponse("<h1>Hello this is index page </h1>")
    return render(request,"home.html",data)

def about(request):
    # return HttpResponse("<h1>this is about page </h1>")
    return render(request,"about.html",{})

def services(request):
    # yo=datetime.datetime.now()
    # return HttpResponse(yo)
    return render(request,"services.html",{})
