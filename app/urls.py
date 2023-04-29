from django.urls import path
from .views import home
from .views import drag_drop
from .views import subir_imagenes

urlpatterns = [
    path('', home, name="home"),
    path('drag_drop/', drag_drop, name="drag_drop"),
    path('subir_imagenes/', subir_imagenes, name="subir_imagenes"),
]