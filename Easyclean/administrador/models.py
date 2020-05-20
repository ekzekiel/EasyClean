from django.db import models

# Create your models here.

class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=50, null=False)
    descricion = models.TextField()
    precio = models.IntegerField(null=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)


