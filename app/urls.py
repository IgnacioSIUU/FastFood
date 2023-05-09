from django.urls import path
from .views import home
from .views import drag_drop
from .views import subir_imagenes
from .views import inicio
from .views import registro

urlpatterns = [
    path('', home, name="home"),
    path('drag_drop/', drag_drop, name="drag_drop"),
    path('subir_imagenes/', subir_imagenes, name="subir_imagenes"),
    path('inicio/', inicio, name="inicio"),
    path('registro/', registro, name="registro"),
]