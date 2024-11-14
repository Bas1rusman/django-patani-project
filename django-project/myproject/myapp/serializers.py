from rest_framework import serializers
from .models import Item 
from .models import Person
from .models import Proyek
from .models import Petani


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class ProyekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyek
        fields = '__all__'

class PetaniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petani
        fields = '__all__'


