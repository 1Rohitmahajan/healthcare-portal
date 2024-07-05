from django.contrib import admin
from youcare.models import contact
from .models import Insurance, Register
from youcare.models import Cont, Doctor, PatientAppointment
# from youcare.models import Appointment
# Register your models here.


admin.site.register(contact)
admin.site.register(Register)
admin.site.register(Cont)
admin.site.register(Doctor)
admin.site.register(PatientAppointment)
admin.site.register(Insurance)


# admin.site.register(Appointment)
