from rest_framework import serializers
from .models import *

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'fullName', 'address', 'phoneNumber', 'age', 'email']


class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ['id', 'Full_Name', 'email', 'specialty']

class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id','Full_Name','email','phoneNumber', 'appointmentDate', 'doctors', 'department', 'message']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['id', 'name', 'description']