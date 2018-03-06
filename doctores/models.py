from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from auth.models import BaseModelAuditoria


class Doctores(BaseModelAuditoria):
    nombres = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=200)
    apellido_materno = models.CharField(max_length=200)
    edad = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
