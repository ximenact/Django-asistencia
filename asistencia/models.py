from django.db import models

# Create your models here.
class asistencia(models.Model):
    tipo_documento = models.CharField(max_length = 30)
    documento = models.CharField(max_length=100)
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    whatsapp = models.CharField(max_length = 20)
    fecha = models.DateField()
    asistio = models.BooleanField()

    def __str__(self):
        return self.nombre