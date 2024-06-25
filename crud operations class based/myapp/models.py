from django.db import models

# Create your models here.

class Userdetails(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField()
    contact = models.IntegerField()
    quotes = models.TextField()

    def __str__(self):
        return self.name





#relationship
class Department(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name



class Person(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name="department")
    dob = models.DateField()
    email = models.EmailField()
    contact = models.IntegerField()
    quotes = models.TextField()

    def __str__(self):
        return self.name
