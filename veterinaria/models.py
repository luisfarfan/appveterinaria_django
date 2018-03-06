from django.db import models

from auth.models import BaseModelAuditoria


class Veterinaria(BaseModelAuditoria):
    nombre = models.CharField(max_length=200)
    tipo_veterinaria = models.ForeignKey('TipoVeterinaria', default=1)  # por defecto todas seran veterinarias unicas
    veterinaria_sede = models.ForeignKey('Veterinaria', null=True)


# ToDo el nombre deberia cambiarse a algo mas referido a lo que se quiere
# TipoVeterinaria trata sobre si una veterinaria derrepente es una cadena de veterinarias, o solo es una.
# podria llamarse como una marca.
class TipoVeterinaria(models.Model):
    nombre = models.CharField(max_length=100)
