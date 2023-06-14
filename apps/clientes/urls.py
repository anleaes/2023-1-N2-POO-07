from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'clientes'

router = routers.DefaultRouter()
router.register('clientes', views.ClientesViewSet, basename='clientes')

urlpatterns = [
    path('', include(router.urls) )
]
