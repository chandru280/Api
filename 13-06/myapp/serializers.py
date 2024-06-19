from rest_framework import serializers
from myapp.models import (Userdetails)

class UserdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdetails
        fields = '__all__'
