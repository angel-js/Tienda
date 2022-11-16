from django.contrib import admin
from .models import Cliente, Producto, Categoria

#Definicón de modelos relacionados
class ProductoInline(admin.TabularInline):
    model = Producto
    #Eliminar los productos extras vacíos
    extra = 0
    
# Define la clase admin para Cliente
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'fecha_nac', 'edad', 'correo')
    list_filter = ('apellido', 'fecha_nac')
    fieldsets = (
        ('Identificación',{
            'fields':('nombre', 'apellido')
        }),
        ('Información Adicional',{
            'fields':('fecha_nac', 'edad', 'correo')
        }),
    )

# Define la clase admin para Producto
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'stock')
    list_filter = ('nombre',)
    
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria')
    list_filter = ('categoria',)
    #Permite desplegar los productos Asociados a la categoría.
    inlines = [ProductoInline]
    
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)