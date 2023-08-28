from django.contrib import admin

# Register your models here.

from hospitalapp.forms import DoctorDetailsForm
#admin reg
from  .models import DoctorDetails 
@admin.register(DoctorDetails)
class DoctorDetailsAdmin(admin.ModelAdmin):
    list_display =('name','email','phone','nid','area','special','daywork')


from  .models import Patient
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display=('doctor_name','name','phone','email','location','patient_category','details') 





   



