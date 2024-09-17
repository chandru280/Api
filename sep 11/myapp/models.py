from django.db import models

 
class Person(models.Model):
    name = models.CharField(max_length=20)
    register = models.CharField(max_length=20, unique=True, default=0)
    department = models.CharField(max_length=20)
    dob = models.DateField(auto_now=False, auto_now_add=False)
   
    def __str__(self):
        return f"{self.name} ({self.register}) {self.department}"
