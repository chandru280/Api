from rest_framework import generics
from .models import *
from .serializers import PersonSerializer

class PersonCreateView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonListView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer 


class PersonRetrieveView(generics.RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'id' 

class PersonDestroyView(generics.DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'id' 


class PersonUpdateView(generics.UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'id' 
    

class PersonListCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer 


class PersonRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer 
    lookup_field = 'id' 


class PersonRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer 
    lookup_field = 'id' 


class PersonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer 
    lookup_field = 'id' 
