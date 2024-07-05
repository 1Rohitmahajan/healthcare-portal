from django.db import models
from django.contrib.auth.models import User

# Create your models here.
departments = [('Cardiologist', 'Cardiologist'),
               ('Dermatologists', 'Dermatologists'),
               ('Emergency Medicine Specialists',
                'Emergency Medicine Specialists'),
               ('Allergists/Immunologists', 'Allergists/Immunologists'),
               ('Anesthesiologists', 'Anesthesiologists'),
               ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')
               ]


class contact(models.Model):
    name = models.CharField(null=False, blank=False, max_length=122)
    email = models.CharField(null=False, blank=False, max_length=122)
    phone = models.CharField(null=False, blank=False, max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Register(models.Model):
    first_name = models.CharField(max_length=122)
    last_name = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=122)
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=18)

    def __str__(self):
        return self.username


class Cont(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField(null=False, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=100)  # Field for the doctor's name
    profile_pic = models.ImageField(
        upload_to='profile_pic/DoctorProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    department = models.CharField(
        max_length=50, choices=departments, default='Cardiologist')
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.doctor_name} ({self.department})"



class PatientAppointment(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    # Fields for patient information
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(null=False, blank=False, max_length=122)
    last_name = models.CharField(null=False, blank=False, max_length=122)
    phone = models.CharField(null=False, blank=False, max_length=12)
    age = models.CharField(null=False, blank=False, max_length=12)
    address = models.CharField(null=False, blank=False, max_length=18)
    
    date = models.DateTimeField(auto_now=True)
    dieses = models.CharField(null=False, blank=False, max_length=18)
    symptoms = models.CharField(null=False, blank=False, max_length=18)

    # Field to assign a doctor to the appointment

    assigned_doctors = models.ManyToManyField(Doctor, related_name='appointments')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.dieses}"





class Insurance(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    rate = models.CharField(max_length=12)
    desc = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
