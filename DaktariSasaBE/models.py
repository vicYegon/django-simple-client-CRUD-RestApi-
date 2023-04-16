from django.db import models

class Patient(models.Model):
    fullName = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    phoneNumber = models.IntegerField()


    def __str__(self):
        return self.fullName