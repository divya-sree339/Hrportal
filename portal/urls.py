from django.urls import path
from . import views

urlpatterns = [
    path('demo/', views.demo),
    path('home/', views.home_page),
    path('registration/', views.registration),
    path('login/', views.userlogin),
    path('logout/', views.userlogout),
    path('emp_list/',views.employee_list),
    path('<int:empid>/',views.employee_details),
    path('department/', views.department),
    path('depform/',views.department_form)
]
