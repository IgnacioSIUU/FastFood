from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def drag_drop(request):
    return render(request, 'app/drag_drop.html')

def subir_imagenes(request):
    return render(request, 'app/subir_imagenes.php')
def inicio(request):
    return render(request, 'app/inicio.html')
def registro(request):
    return render(request, 'app/registro.html')
