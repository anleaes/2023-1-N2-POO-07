from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'animais'

router = routers.DefaultRouter()
router.register('animais', views.AnimaisViewSet, basename='animais')

urlpatterns = [
    path('', include(router.urls) )
]