from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from .models import Person, Userdetails, Department
from .serializers import (UserdetailsmodelSerializer, 
                          PersondetailsmodelSerializer, DepartmentdetailsmodelSerializer)

from rest_framework.views import APIView


def helloworld(request):
    data = {
        "Message": "Hello chan"
    }

    return JsonResponse(data)


class DepartmentView(APIView):
    def get(self, request):
        all = Department.objects.all()
        serializer = DepartmentdetailsmodelSerializer(all, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = DepartmentdetailsmodelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)


class UserView(APIView):
    def get(self, request):
        all = Userdetails.objects.all()
        serializer = UserdetailsmodelSerializer(all, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = UserdetailsmodelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)




class UserDetailView(APIView):
    def get(self, request, pk):
        all = Userdetails.objects.get(pk=pk)
        serializer = UserdetailsmodelSerializer(all)
        return Response(serializer.data)

    def put(self, request, pk):
        all = Userdetails.objects.get(pk=pk)
        serializer = UserdetailsmodelSerializer(all, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)

    def delete(self, request, pk):
        all = Userdetails.objects.get(pk=pk)
        all.delete()
        return Response()









class PersonView(APIView):
    def get(self, request):
        all = Person.objects.all()
        serializer = PersondetailsmodelSerializer(all, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PersondetailsmodelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)




class PersonDetailView(APIView):
    def get(self, request, pk):
        all = Person.objects.get(pk=pk)
        serializer = PersondetailsmodelSerializer(all)
        return Response(serializer.data)

    def put(self, request, pk):
        all = Person.objects.get(pk=pk)
        serializer = PersondetailsmodelSerializer(all, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)

    def delete(self, request, pk):
        all = Person.objects.get(pk=pk)
        all.delete()
        return Response()










