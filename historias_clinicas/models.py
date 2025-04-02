from django.db import models

# Create your models here.
from django.db import models

class HistoriaClinica(models.Model):
    nombre_paciente = models.CharField(max_length=255)
    edad = models.CharField(max_length=10)
    identificacion = models.CharField(max_length=50, unique=True, primary_key=True)
    procedencia = models.CharField(max_length=255)
    ocupacion = models.CharField(max_length=255)
    acompanante = models.CharField(max_length=255, blank=True, null=True)
    motivo_consulta = models.TextField()
    enfermedad_actual = models.CharField(max_length=255, blank=True, null=True)
    antecedentes_patologicos = models.TextField(blank=True, null=True)
    antecedentes_farmacologicos = models.TextField(blank=True, null=True)
    antecedentes_alergicos = models.TextField(blank=True, null=True)
    plan_de_manejo= models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_paciente
