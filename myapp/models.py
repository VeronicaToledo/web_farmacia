from django.db import models

class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
