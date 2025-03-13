from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class HistoriaClinica(models.Model):
    id = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    genero = models.CharField(max_length=5)
    tSangre = models.CharField(max_length=5)
    alergias = JSONField(default=list)
    cMedicas = JSONField(default=list)
    
def __str__(self):
    return f"{self.nombre} - {self.edad} años - Tipo de sangre: {self.tSangre}"


