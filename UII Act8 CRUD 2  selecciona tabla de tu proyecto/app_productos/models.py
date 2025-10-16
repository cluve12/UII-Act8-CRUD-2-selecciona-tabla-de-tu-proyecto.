from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f'Producto: {self.nombre} - ${self.precio}'