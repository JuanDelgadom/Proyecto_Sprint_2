from django.db import models

# Create your models here.

class HistoriaClinica(models.Model):
    paciente_id = models.IntegerField()
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField()
    fecha = models.DateField()
