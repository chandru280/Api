from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Userdetails
from .serializers import UserdetailsmodelSerializer




def helloworld(request):
    data = {
        "Message": "Hello chan"
    }

    return JsonResponse(data)



@api_view(['GET', 'POST'])
def demo(request):
    if request.method == "GET":
        all = Userdetails.objects.all()
        serializer = UserdetailsmodelSerializer(all, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = UserdetailsmodelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)



@api_view(['GET', 'PUT', 'DELETE'])
def demo1(request,pk):
    if request.method == "GET":
        all = Userdetails.objects.get(pk=pk)
        serializer = UserdetailsmodelSerializer(all)
        return Response(serializer.data)

    if request.method == "PUT":
        all = Userdetails.objects.get(pk=pk)
        serializer = UserdetailsmodelSerializer(all, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)

    if request.method == "DELETE":
        all = Userdetails.objects.get(pk=pk)
        all.delete()
        return Response()



























