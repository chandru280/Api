from django.db import models

# Create your models here.

class Userdetails(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField()
    contact = models.IntegerField()
    quotes = models.TextField()















from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    
    USER_ROLE = [("admin","admin"),("moderator","moderator"),("normal_user","normal_user")]

    email = models.EmailField(unique=True)
    phone_number = models.IntegerField()
    address = models.TextField()

    role = models.CharField(choices=USER_ROLE,max_length=20)


    REQUIRED_FIELDS = ["phone_number", "email"]  
    


#     {
# "username": "chandru",
# "password": "chan@7339", 
# "email": "icecse2028@gmail.com",
# "phone_number": "7339143040",
# }