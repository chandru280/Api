from django.db import models

# Create your models here.

class Userdetails(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField()
    contact = models.IntegerField()
    quotes = models.TextField()
