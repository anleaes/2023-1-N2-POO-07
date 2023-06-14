from .models import Animais
from rest_framework import serializers

class AnimaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animais
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']