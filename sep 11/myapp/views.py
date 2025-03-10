from rest_framework import generics
from .models import *
from .serializers import PersonSerializer


from rest_framework.response import Response
from rest_framework import status

# class PersonCreateView(generics.CreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer


class PersonCreateView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)     # Get the serializer with the request data
        serializer.is_valid(raise_exception=True)  # Check the validation if not valid it return 400 bad request
        
         # Validate the data without saving
        if serializer.is_valid():
            # Extract and print the fields
            name = serializer.validated_data.get('name')
            register = serializer.validated_data.get('register')
            department = serializer.validated_data.get('department')
            dob = serializer.validated_data.get('dob')

            # Print the fields (in a real-world scenario, use logging)
            print(f"Name: {name}")
            print(f"Register: {register}")
            print(f"Department: {department}")
            print(f"Date of Birth: {dob}")
            
        self.perform_create(serializer) # Save the validated data to the database
        
        
        response_data = {
            'message': 'Data added successfully',
            'data': serializer.data
        }
        
        return Response(response_data, status=status.HTTP_201_CREATED)


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






'''<----------------------------------- Router Code ----------------------------------->'''
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from .models import Book
from .serializers import BookSerializer

class BookViewSet2(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Customizing the list method
    def list(self, request, *args, **kwargs):
        # Custom behavior: Only list books published after 2000
        books = Book.objects.filter(published_date__year__gt=2000)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    # Customizing the retrieve method
    def retrieve(self, request, *args, **kwargs):
        # Custom behavior: Add a custom message to the response
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        data['message'] = "Custom retrieve message"
        return Response(data)

    # Customizing the create method
    def create(self, request, *args, **kwargs):
        # Custom behavior: Add validation before creating an object
        if 'isbn' in request.data and len(request.data['isbn']) != 13:
            return Response({"error": "ISBN must be 13 characters long."}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    # Customizing the update method
    def update(self, request, *args, **kwargs):
        # Custom behavior: Modify the title before saving
        request.data['title'] = request.data['title'].upper()
        return super().update(request, *args, **kwargs)

    # Customizing the partial_update method
    def partial_update(self, request, *args, **kwargs):
        # Custom behavior: Log the partial update
        print(f"Partial update on book with ID: {kwargs['pk']}")
        return super().partial_update(request, *args, **kwargs)

    # Customizing the destroy method
    def destroy(self, request, *args, **kwargs):
        # Custom behavior: Prevent deletion if the book was published before 2000
        instance = self.get_object()
        if instance.published_date.year < 2000:
            return Response({"error": "Cannot delete books published before 2000."}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)

    # Adding a custom action
    @action(detail=False, methods=['get'])
    def recent(self, request):
        # Custom action: Return books published in the last 5 years
        recent_books = Book.objects.filter(published_date__year__gte=(timezone.now().year - 5))
        serializer = self.get_serializer(recent_books, many=True)
        return Response(serializer.data)


'''

Works with Routers:

ModelViewSet
ReadOnlyModelViewSet
ViewSet
GenericViewSet

Does Not Typically Use Routers:

APIView
GenericAPIView
ListAPIView
CreateAPIView
RetrieveAPIView
UpdateAPIView
DestroyAPIView

'''