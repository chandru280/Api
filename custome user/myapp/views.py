from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def helloworld(request):
    data = {
        "Message": "Hello chan"
    }

    return JsonResponse(data)



from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Userdetails
from .serializers import UserdetailsSerializer




@api_view(['GET', 'POST'])
def demo(request):
    if request.method == "GET":
        all = Userdetails.objects.all()
        serializer = UserdetailsSerializer(all, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = UserdetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)



@api_view(['GET'])
def demo1(request,pk):
    all = Userdetails.objects.get(pk=pk)
    serializer = UserdetailsSerializer(all)
    return Response(serializer.data)









































# CREATE
@api_view(['POST'])
def create_item(request):
    if request.method == 'POST':
        serializer = UserdetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# READ
@api_view(['GET'])
def get_items(request):
    if request.method == 'GET':
        items = Userdetails.objects.all()
        serializer = UserdetailsSerializer(items, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_item(request, pk):
    try:
        item = Userdetails.objects.get(pk=pk)
    except Userdetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserdetailsSerializer(item)
        return Response(serializer.data)

# UPDATE
@api_view(['PUT'])
def update_item(request, pk):
    try:
        item = Userdetails.objects.get(pk=pk)
    except Userdetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserdetailsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE
@api_view(['DELETE'])
def delete_item(request, pk):
    try:
        item = Userdetails.objects.get(pk=pk)
    except Userdetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)














