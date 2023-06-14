from .models import Adocoes
from rest_framework import viewsets
from .serializers import AdocoesSerializer

class AdocoesViewSet(viewsets.ModelViewSet):
    queryset = Adocoes.objects.all()
    serializer_class = AdocoesSerializer  