from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Employee, Department
from .forms import DepartmentForm


# Create your views here.


def demo(request):
    return HttpResponse("Welcome to Django Sessions")


def home_page(request):
    return render(request, "home.html")


def registration(request):
    if request.method == "POST":
        print(request.POST, request.FILES)
        dept = Department.objects.get(dept_name=request.POST['dept_name'])
        username = request.POST['user_name']
        user = User.objects.create_user(
            first_name=request.POST['firstname'],
            last_name=request.POST['lastname'],
            username=username,
            email=request.POST['email'],
            password=request.POST['password'],
        )
        Employee.objects.create(
            name=request.POST['firstname'] + " " + request.POST['lastname'],
            user=user,
            mobile=request.POST['mobile'],
            address=request.POST['address'],
            doj=request.POST['doj'],
            dept=dept,
            designation=request.POST['designation'],
            image=request.FILES['image'],
        )
    dept = Department.objects.all()
    return render(request, "registration.html", {"dept": dept})


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
    emp_list = Employee.objects.all()
    return render(request, "employee_list.html", {"emp_list": emp_list})


def employee_details(request, empid):
    details = Employee.objects.get(id=empid)
    return render(request, "employee_details.html", {"emp_details": details})


def department(request):
    if request.method == "POST":
        print(request.POST)
        Department.objects.create(
            dept_name=request.POST['dept_name'],
            dept_desc=request.POST['dept_description']

        )
        return HttpResponse("Success")
    return render(request, "department.html")


def department_form(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            return HttpResponse("Successfully Added")

    form = DepartmentForm()
    return render(request, "departmentform.html", {'depform': form})
