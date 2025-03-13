from django.db import models

# Create your models here.

class HistoriaClinica(models.Model):
    id = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    tSangre = models.CharField(max_length=5)
    alergias = models.JSONField(default=list)
    cMedicas = models.JSONField(default=list)
    
def __str__(self):
    return f"{self.nombre} - {self.edad} años - Tipo de sangre: {self.tSangre}"
