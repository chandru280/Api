from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def helloworld(request):
    data = {
        "Message": "Hello chan"
    }

    return JsonResponse(data)