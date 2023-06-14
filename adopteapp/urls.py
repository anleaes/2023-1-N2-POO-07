from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adocoes/', include('adocoes.urls', namespace='adocoes')),
    path('clientes/', include('clientes.urls', namespace='clientes')),
    path('animais/', include('animais.urls', namespace='animais')),
    path('porte_animal/', include('porte_animal.urls', namespace='porte_animal')),
    
]
