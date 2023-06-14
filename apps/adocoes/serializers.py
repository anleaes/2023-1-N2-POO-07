from .models import Adocoes
from rest_framework import serializers

class AdocoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adocoes
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']