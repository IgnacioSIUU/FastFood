from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="marcas", null=True)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre