from django.shortcuts import render,reverse, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login, logout
from datetime import datetime

from django.contrib import messages
from youcare.models import Cont, Doctor, PatientAppointment, Insurance
# from youcare.models import Appointment
# from .models import patient_view
from .models import Insurance, Register

# Create your views here
# superuser rohitam35@gmail.com
# # password Rohit@123


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def homeservices(request):
    return render(request, 'homeservices.html')


def dieses(request):
    return render(request, 'dieses.html')



def insurance(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        rate = request.POST.get('rate')

        desc = request.POST.get('desc')
        contact = Insurance(name=name, email=email, phone=phone, rate=rate,
                            desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your request send successfully')

    return render(request, 'insurance.html')


def listmedicine(request):
    return render(request, 'listmedicine.html')


def contact1(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        desc = request.POST.get('desc')
        contact1 = Cont(name=name, email=email, phone=phone,
                        desc=desc, date=datetime.today())
        contact1.save()
        messages.success(request, 'Your request send successfully')

    return render(request, 'contact1.html')


def doctor(request):
    return render(request, 'doctor.html')

def admin_approve_doctor(request):
    return render(request,'admin_approve_doctor.html')

def admin_view_doctor_specialisation(request):
    return render(request,'admin_view_doctor_specialisation.html')



def register_patient(request):
    return render(request, 'register_patient.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email ']
        password = request.POST['password']
        password2 = request.POST['password2']
        if len(username) <= 10:
            if password == password2 and len(password) >= 8:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already taken')
                    return HttpResponse("404 - Not found")

                elif not username.isalnum():
                    messages.error(
                        request, "User name should only contain letters and numbers")
                    return HttpResponse("404 - Not found")

                else:
                    user = User.objects.create_user(
                        first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.save()
                    messages.success(request, 'Registeration successfully')
                    return render(request, 'register_patient.html')
            else:
                messages.info(request, 'password not same ')
                return redirect('register_patient')
        else:
            messages.info(request, 'Username less than character number ')
            return HttpResponse("404 - Not found")

    else:
        return HttpResponse("404 - Not found")


def logoutuser(request):
    logout(request)
    messages.success(request, 'Logout successfully')
    return redirect('/')


def loginuser(request):
    if request.user.is_authenticated:
            return redirect('/appointment_dashboard') 
    elif request.method == "POST":
        username = request.POST['username']
        password2 = request.POST['password2']
        
        user = authenticate(request, username=username, password=password2)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/appointment_dashboard')

        else:
            messages.info(request, 'invalid credentials')
            return render(request, 'register_patient.html')
    else:
        return HttpResponse("404-Not found")


def appointment_dashboard(request):
    return render(request, 'appointment_dashboard.html')
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        age = request.POST.get('age')
        dieses = request.POST.get('dieses')
        address = request.POST.get('address')

        appointment = Appointment(first_name=first_name, last_name=last_name, phone=phone,
                                  address=address, date=date, dieses=dieses, age=age)
        appointment.save()
        messages.success(request, 'appointment saved successfully')
        return HttpResponse("403 error")
    return render(request, 'application.html')


def patient_add_appointment(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        age = request.POST.get('age')
        dieses = request.POST.get('dieses')
        address = request.POST.get('address')
        symptoms = request.POST.get('symptoms')
        doctor_name = request.POST.get('doctor_name')

        appointment = PatientAppointment(first_name=first_name, last_name=last_name, phone=phone,
                                         address=address, date=date, dieses=dieses, age=age, symptoms=symptoms, doctor_name=doctor_name)
        appointment.save()
        messages.success(request, 'appointment saved successfully')
    doct = Doctor()
    context = {'doct': doct}    
    return render(request, 'patient_add_appointment.html',context)


from django.shortcuts import render, redirect
from .forms import DoctorForm

def admin_add_doctor_view(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
       
        form.save()
             # Redirect to doctor list view after successful creation
    else:
        form = DoctorForm()  # If GET request, create a new form

    return render(request, 'admin_add_doctor.html', {'form': form})



def admin_view_doctor(request):
    appointments = Doctor.objects.all()
    context = {'appointments': appointments}
    return render(request,'admin_view_doctor.html',context)


def patient_approve_appointment(request):
    appointments = PatientAppointment.objects.all()
    context = {'appointments': appointments}
    
    return render(request, 'patient_approve_appointment.html',context)


def patient_view_appointment(request):
    appointments = PatientAppointment.objects.all()
    context = {'appointments': appointments}
    
    return render(request, 'patient_view_appointment.html',context)

def approve_appointment(request, appointment_id):
    appointment = get_object_or_404(PatientAppointment, id=appointment_id)
    appointment.status = 'Approved'
    appointment.save()
    return redirect(reverse('appointment_list'))  # Redirect to the appointment list view after approving

# View for rejecting an appointment
def reject_appointment(request, appointment_id):
    appointment = get_object_or_404(PatientAppointment, id=appointment_id)
    appointment.status = 'Rejected'
    delete_appointment(request,appointment_id)
    appointment.save()
    return redirect(reverse('patient_approve_appointment')) 


def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(PatientAppointment, pk=appointment_id)

    if request.method == 'POST':
        appointment.delete()
        return redirect('patient_view_appointment.html')  # Replace 'appointments_list' with your actual URL name
    return redirect('/appointment_dashboard')

