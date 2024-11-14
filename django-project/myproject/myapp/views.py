from django.shortcuts import render
from rest_framework import generics
from .models import Item 
from .models import Person 
from .models import Proyek
from .models import Petani
from .serializers import ItemSerializer
from .serializers import PersonSerializer
from .serializers import ProyekSerializer
from .serializers import PetaniSerializer


def index(request):
    return render(request, 'index.html')


class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class PersonListCreate(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ProyekListCreate(generics.ListCreateAPIView):
    queryset = Proyek.objects.all()
    serializer_class = ProyekSerializer

class ProyekDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proyek.objects.all()
    serializer_class = ProyekSerializer

class PetaniListCreate(generics.ListCreateAPIView):
    queryset = Petani.objects.all()
    serializer_class = PetaniSerializer

class PetaniDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Petani.objects.all()
    serializer_class = PetaniSerializer









