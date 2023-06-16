from django.db import models

class Patient(models.Model):
    fullName = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    phoneNumber = models.IntegerField()
    age = models.IntegerField(null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.fullName
    
    class Meta:
        verbose_name_plural = "Patients"
    
class Doctors(models.Model):
    Full_Name = models.CharField(max_length= 200)
    email = models.EmailField()
    specialty = models.CharField(max_length=500)

    def __str__(self):
        return self.Full_Name
    
    class Meta:
        verbose_name_plural = "Doctors"
    
class Departments(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
 
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Departments"

class Appointment(models.Model):
    Full_Name = models.CharField(max_length=200)
    email = models.EmailField()
    phoneNumber = models.IntegerField()
    appointmentDate = models.DateField(auto_now_add=True)
    doctor = models.ForeignKey('Doctors', on_delete=models.CASCADE)
    department = models.ForeignKey('Departments', on_delete=models.CASCADE)
    message = models.TextField(null=True)

    def __str__(self):
        return self.appointmentDate
    
    class Meta:
        verbose_name_plural = "Appointments"
    
