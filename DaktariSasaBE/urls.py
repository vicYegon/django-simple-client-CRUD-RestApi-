"""
URL configuration for DaktariSasaBE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from DaktariSasaBE import views
# from rest_framework.routers import DefaultRouter
# from .views import doctors_list


# router = DefaultRouter()
# router.register(r'doctors', doctors_list, basename='doctors')

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('DaktariSasaBE/patients', views.patient_list),
    path('DaktariSasaBE/<int:id>', views.patient_details),
    path('DaktariSasaBE/doctors', views.doctors_list),
    path('DaktariSasaBE/<int:id>', views.doctor_details),
    path('DaktariSasaBE/appointments', views.appointments_list),
    path('DaktariSasaBE/<int:id>', views.appointment_details),
    path('DaktariSasaBE/departments', views.department_list),
    path('DaktariSasaBE/<int:id>', views.department_details),
    # path('api/', include(router.urls))
]
