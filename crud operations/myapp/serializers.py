from rest_framework import serializers
from myapp.models import (Userdetails)




#Normal Serializers
class UserdetailsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    dob = serializers.DateField()
    email = serializers.EmailField()
    contact = serializers.IntegerField()
    quotes = serializers.CharField()
    

    def create(self, validated_data):
        return Userdetails.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.email = validated_data.get('email', instance.email)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.quotes = validated_data.get('quotes', instance.quotes)
        instance.save()
        return instance




#Model Serializers
class UserdetailsmodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdetails
        fields = '__all__'
        exclude = ['']

