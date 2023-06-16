from django.contrib import admin
from .models import *

admin.site.register(Patient)
admin.site.register(Doctors)
admin.site.register(Appointment)
admin.site.register(Departments)
