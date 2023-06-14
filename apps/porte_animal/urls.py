from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'porte_animal'

router = routers.DefaultRouter()
router.register('porte_animal', views.PorteAnimalViewSet, basename='porte_animal')

urlpatterns = [
    path('', include(router.urls) )
]