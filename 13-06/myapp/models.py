from django.db import models
from django.db.models.signals import pre_save, post_save
 
 
# from rest_framework.authtoken.models import Token

# class BlacklistedToken(models.Model):
#     token = models.OneToOneField(Token, on_delete=models.CASCADE)
#     blacklisted_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.token.key

 
class Population(models.Model):
    country = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    human_count = models.PositiveBigIntegerField()

def image_collection_path(instance, file_name):
    return f"image_collection/{file_name}"

class ImageCollection(models.Model):
    image = models.FileField(upload_to=image_collection_path)
    notes = models.TextField()


class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)