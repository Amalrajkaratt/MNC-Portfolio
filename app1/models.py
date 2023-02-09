from django.db import models

# Create your models here.

# Client Service Signup
class ServiceSigup(models.Model):
    Name=models.CharField(max_length=16)
    Designation=models.CharField(max_length=16)
    CompanyName=models.CharField(max_length=20)
    ContactEmail=models.EmailField()
    ContactNumber=models.IntegerField()
    ServiceType=models.CharField(max_length=15)
    ServiceDetails=models.CharField(max_length=200)
    Password=models.CharField(max_length=8)

# Job seekers signup
class CareerSignup(models.Model):
    Name=models.CharField(max_length=16)
    Email=models.EmailField()
    ContactNumber=models.IntegerField()
    DOB=models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Qualification=models.CharField(max_length=20)
    InstituteName=models.CharField(max_length=20)
    YearOfPassing=models.IntegerField()
    Password=models.CharField(max_length=8)