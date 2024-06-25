from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from .models import Userdetails
from .serializers import UserdetailsmodelSerializer

from rest_framework.views import APIView


def helloworld(request):
    data = {
        "Message": "Hello chan"
    }

    return JsonResponse(data)



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










