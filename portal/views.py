from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Employee


# Create your views here.


def demo(request):
    return HttpResponse("Welcome to Django Sessions")


def home_page(request):
    return render(request, "home.html")


def registration(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST['user_name']
        user = User.objects.create_user(
            first_name=request.POST['firstname'],
            last_name=request.POST['lastname'],
            username=username,
            email=request.POST['email'],
            password=request.POST['password'],
        )
        Employee.objects.create(
            name=request.POST['firstname']+" "+request.POST['lastname'],
            user=user,
            mobile=request.POST['mobile'],
            address=request.POST['address'],
            doj=request.POST['doj'],
            designation=request.POST['designation'],
            image=request.FILES['image'],
        )
    return render(request, "registration.html")


def userlogin(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['user_name'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/portal/emp_list/")
        # A backend authenticated the credentials
        else:
            return HttpResponse("Login Failed")
    # No backend authenticated the credentials
    return render(request, "login.html")


def userlogout(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/portal/login/")


def employee_list(request):
    emp_list=Employee.objects.all()
    return render(request, "employee_list.html",{"emp_list":emp_list})


def employee_details(request,empid):
    details=Employee.objects.get(id=empid)
    return render(request, "employee_details.html",{"emp_details":details})
