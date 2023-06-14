from .models import PorteAnimal
from rest_framework import serializers

class PorteAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PorteAnimal
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']