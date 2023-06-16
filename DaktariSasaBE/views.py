# from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, action
from rest_framework.response import Response    
from rest_framework import status
# ------------------------------------------------------------------------------------------------------------#
# read,write patient's data
#--------------------------------------------------------------------------------------------------------------#




@api_view(['GET', 'POST']) #decorator
def patient_list(request):
    
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
# --------------------------------------------------------------------------------------------------------- #
# Read, update and delete patient's data
# ----------------------------------------------------------------------------------------------------------#
@api_view(['GET', 'PUT', 'DELETE'])
def patient_details(request, id):
    try:
        patient = Patient.objects.get(pk=id)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# -------------------------------------------------------------------------------------------------------------------#

# read and write doctors data
@api_view(['GET', 'POST']) #decorator
def doctors_list(request):
    
    if request.method == 'GET':
        doctors = Doctors.objects.all()
        serializer = DoctorsSerializer(doctors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DoctorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def doctor_details(request, id):
    try:
        doctors = Doctors.objects.get(pk=id)
    except Doctors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DoctorsSerializer(doctors)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DoctorsSerializer(doctors, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        doctors.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# -------------------------------------------------------------------------------------------------------#
# appointments api #

@api_view(['GET', 'POST']) #decorator
def appointments_list(request):
    
    if request.method == 'GET':
        appointments = Appointment.objects.all()
        serializer = AppointmentsSerializer(appointments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AppointmentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def appointment_details(request, id):
    try:
        appointments = Appointment.objects.get(pk=id)
    except Appointment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppointmentsSerializer(appointments)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AppointmentsSerializer(appointments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        appointments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------------------------------------------------------------------------------------------------#
# Departments Api #

@api_view(['GET', 'POST']) #decorator
def department_list(request):
    
    if request.method == 'GET':
        departments = Departments.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def department_details(request, id):
    try:
        departments = Departments.objects.get(pk=id)
    except Departments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DepartmentSerializer(departments)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DepartmentSerializer(departments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        departments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# ----------------------------------------------------------------------------------------------------#
# Login Api













#----------------------------------------------------------------------------------------------------#
# Registration Api
