from django.shortcuts import render
from django.http import JsonResponse


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.core.files.base import ContentFile
from .models import Population, ImageCollection, Note
# import requests
from myapp.serializers import NoteSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



def helloworld(request):
    data = {
        "Message": "Hello chan"
    }

    return JsonResponse(data)
 

class Notes(APIView):
     
    # create
    def post(self, request):
        data = request.data
        title = data["title"]
        description = data["description"]
        # note = Note.objects.create(title=title, description=description)
        # note = Note()
        # note.title = title
        # note.description = description
        # note.save()
        note = Note(title=title, description=description)
        note.save()
        note_data = {
            "title": note.title,
            "description": note.description,
        }
        return Response(data=note_data, status=status.HTTP_201_CREATED)

    # get
    def get(self, request):
        notes = Note.objects.filter(is_active=True)
        data = NoteSerializer(instance=notes, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)




    # update
    def put(self, request):
        data = request.data
        note_id = data["note_id"]
        title = data["title"]
        description = data["description"]
        note = Note.objects.get(id=note_id)
        note.title = title
        note.description = description
        note.save()
        note_data = NoteSerializer(instance=note, many=False)
        return Response(data=note_data.data, status=status.HTTP_200_OK)


    # delete
    def delete(self, request):
        note_id = request.data["note_id"]
        # # method 1
        # note = Note.objects.get(id=note_id)
        # note.is_active = False
        # note.save()

        # method 2
        note = Note.objects.get(id=note_id)
        note.delete()
        return Response(data={"note_id": note_id}, status=status.HTTP_200_OK)


class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        print(username, " => ", password)
        if not User.objects.filter(username=username).exists():
            return Response(data={"message": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.get(username=username)
        if not user.check_password(password):
            return Response(data={"message": "Password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)

        token, created = Token.objects.get_or_create(user=user)
        print(f"token = => {token.key}")
        print(f"created = => {created}")
        data = {"token": token.key}

        return Response(data=data, status=status.HTTP_200_OK)



class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response(
                {"message": "Successfully logged out."},
                status=status.HTTP_200_OK
            )
        except Token.DoesNotExist:
            return Response(
                {"error": "Token does not exist."},
                status=status.HTTP_400_BAD_REQUEST
            )
