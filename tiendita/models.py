from django.db import models

# Create your models here.
class Cliente(models.Model):
    """Modelo que representa un cliente."""
    nombre = models.CharField(max_length=200, help_text="Ingrese sus nombres")
    apellido = models.CharField(max_length=200, help_text="Ingrese sus apellidos")
    fecha_nac = models.DateField(null=True, blank=True, help_text="Ingrese su fecha de nacimiento")
    edad = models.IntegerField()
    correo = models.EmailField(blank=True, null=True, help_text="Indique un correo válido")

    def __str__(self):
        """String que representa al objeto cliente"""
        return f'{self.nombre} {self.apellido}'

class Producto(models.Model):
    """Modelo que representa un Producto."""

    nombre = models.CharField(max_length=200, help_text="Ingrese el nombre del producto")
    stock = models.IntegerField(help_text="Ingrese cantidad en stock")
    precio = models.IntegerField(null=True, help_text="Ingrese cantidad en stock")  
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL,null=True )
    # ForeignKey, ya que un producto tiene una sola categoría, 
    # pero la misma categoría puede pertenecer a varios productos.
    # 'Categoria' es un string, en vez de un objeto, porque la clase Categoria 
    # aún no ha sido declarada.

    def __str__(self):
        """String que representa al objeto Producto"""
        return f'{self.nombre}'
 
class Categoria(models.Model):
    categoria = models.CharField(max_length=200, help_text="Ingrese el nombre del producto")
    def __str__(self):
        """String que representa al objeto la Categoría"""
        return f'{self.categoria}'