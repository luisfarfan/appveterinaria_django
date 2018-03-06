from django.db import models

class Animales(models.Model):
    nombre = models.CharField(max_length=100)
