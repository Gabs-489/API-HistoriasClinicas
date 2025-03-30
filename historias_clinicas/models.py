from django.db import models

# Create your models here.
from django.db import models

class HistoriaClinica(models.Model):
    identificacion = models.CharField(max_length=50, primary_key=True)
    nombre_paciente = models.CharField(max_length=255)
    edad = models.CharField(max_length=10)
    procedencia = models.CharField(max_length=255)
    ocupacion = models.CharField(max_length=255)
    acompanante = models.CharField(max_length=255, blank=True, null=True)
    motivo_consulta = models.TextField()

    def __str__(self):
        return self.nombre_paciente
