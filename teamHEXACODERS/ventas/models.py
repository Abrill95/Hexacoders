from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precioAnterior = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    cantidad = models.IntegerField()
    imagen_principal = models.ImageField(upload_to='productos/')
    proveedores = models.ManyToManyField(Proveedor, related_name='productos')


    def calcular_descuento(self):
        if self.precioAnterior and self.precioAnterior > 0:
            return round((self.precio * 100) / self.precioAnterior, 0)
        return 0
    def calcular_coutas(self):
        if self.precio and self.precio > 0:
            return round((self.precio / 6), 0)
        return 0


class ImagenProducto(models.Model):
    producto = models.ForeignKey(
        Producto, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='productos/galeria/')


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    celular = models.CharField(max_length=15)
    foto = models.ImageField(upload_to='clientes/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    favoritos = models.ManyToManyField(Producto, related_name='clientes_favoritos', blank=True)

class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Venta {self.id} - {self.producto.nombre} a {self.cliente.nombre}"
