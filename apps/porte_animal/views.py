from .models import PorteAnimal
from rest_framework import viewsets
from .serializer import PorteAnimalSerializer

class PorteAnimalViewSet(viewsets.ModelViewSet):
    queryset = PorteAnimal.objects.all()
    serializer_class = PorteAnimalSerializer
    
