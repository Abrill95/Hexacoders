from django.db import models

class Producto(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precioAnterior = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    cantidad = models.IntegerField()
    imagen_principal = models.ImageField(upload_to='productos/')

    def calcular_descuento(self):
        if self.precioAnterior and self.precioAnterior > 0:  # Verifica que precioAnterior no sea None o 0
            return round((self.precio * 100) / self.precioAnterior, 0)
        return 0  # Devuelve 0 o cualquier valor por defecto si precioAnterior es None o 0
    def calcular_coutas(self):
        if self.precio and self.precio > 0:  # Verifica que precioAnterior no sea None o 0
            return round((self.precio / 6), 0)
        return 0  # Devuelve 0 o cualquier valor por defecto si precioAnterior es None o 0


class ImagenProducto(models.Model):
    producto = models.ForeignKey(
        Producto, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='productos/galeria/')


def __str__(self):
    return self.nombre
