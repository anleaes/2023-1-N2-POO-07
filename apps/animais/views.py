from .models import Animais
from rest_framework import viewsets
from .serializer import AnimaisSerializer

class AnimaisViewSet(viewsets.ModelViewSet):
    queryset = Animais.objects.all()
    serializer_class = AnimaisSerializer

