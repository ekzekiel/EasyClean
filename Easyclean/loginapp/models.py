
from django.db import models


class LoginappPersona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    password = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    comuna = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    email = models.CharField(max_length=45)


