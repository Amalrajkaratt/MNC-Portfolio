from django.db import models

# Create your models here.

# Admin login model
class AdminPage(models.Model):
    UserId=models.CharField(max_length=15)
    Password=models.CharField(max_length=15)

# Adding job model
class Job(models.Model):
    Title=models.CharField(max_length=40)
    Location=models.CharField(max_length=20)
    Decsription=models.CharField(max_length=200)
    Date=models.DateField()

# Team model
class Team(models.Model):
    Image=models.ImageField(upload_to='media/',null=True,blank=True)
    Name=models.CharField(max_length=20)
    Designation=models.CharField(max_length=20)

# Course model
class Course(models.Model):
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Course=models.CharField(max_length=20)
    Name=models.CharField(max_length=20)

# Review model
class Review(models.Model):
    Review=models.CharField(max_length=200)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Name=models.CharField(max_length=20)
    CompanyName=models.CharField(max_length=30)

# Project Summary
class ProjectSummary(models.Model):
    Image=models.ImageField(upload_to='media/',null=True,blank=True)
    OGP=models.IntegerField()
    CP=models.IntegerField()
    SL=models.IntegerField()
    HC=models.IntegerField()