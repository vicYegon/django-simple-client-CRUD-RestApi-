from django.http import JsonResponse
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# read data
@api_view(['GET', 'POST'])
def patient_list(request):
    
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def patient_details(request):
