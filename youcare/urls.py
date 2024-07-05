from django.contrib import admin
from django.urls import path

from youcare import views

urlpatterns = [
    path('', views.index, name="index"),
    
    path('index', views.index, name="index"),

    path('about', views.about, name="about"),

    path('homeservices', views.homeservices, name="homeservices"),

    path('contact1', views.contact1, name="contact1"),

    path('dieses', views.dieses, name="dieses"),

    path('listmedicine', views.listmedicine, name="listmedicine"),

    # path('dashboard', views.dashboard, name="dashboard"),

    #path('application', views.application, name="application"),

    path('register', views.register, name="register"),
    path('register', views.register, name="register"),
    path('loginuser', views.loginuser, name="loginuser"),

    path('logoutuser', views.logoutuser, name="logoutuser"),
 

    path('register_patient', views.register_patient, name="register_patient"),
    path('patient_approve_appointment', views.patient_approve_appointment, name="patient_approve_appointment"),

    path('appointment_dashboard', views.appointment_dashboard,
         name="appointment_dashboard"),
    path('patient_approve_appointment',views.patient_approve_appointment,name="patient_approve_appointment"),

    path('approve_appointment/<int:appointment_id>/', views.approve_appointment, name='approve_appointment'),
    path('reject_appointment/<int:appointment_id>/', views.reject_appointment, name='reject_appointment'),
    path('doctor', views.doctor, name="doctor"),
   #  path('doctor_list/', views.doctor_list_view, name='doctor_list'),
    path('admin_add__doctor', views.admin_add_doctor_view,
         name="admin_add__doctor"),

    path('admin_approve_doctor',views.admin_approve_doctor,name='admin_approve_doctor'),

    path('patient_add_appointment', views.patient_add_appointment,
         name="patient_add_appointment"),
    
    path('admin_view_doctor_specialisation',views.admin_view_doctor_specialisation,name='admin_view_doctor_specialisation'),
    path('admin_view_doctor',views.admin_view_doctor,name='admin_view_doctor'),

    path('insurance', views.insurance, name="insurance"),
    path('patient_view_appointment',
         views.patient_view_appointment, name="patient_view_appointment"),

]
