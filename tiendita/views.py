from django.shortcuts import render
from .models import Cliente, Producto, Categoria
from django.views import generic

# Create your views here.
def index(request):
    """Función vista para la página inicio del sitio."""
    # Genera contadores de algunos de los objetos principales
    cant_clientes=Cliente.objects.all().count()
    cant_productos=Producto.objects.all().count()
    total_categorias=Categoria.objects.count() # El 'all()' esta implícito por defecto.
    # Productos disponibles en Pinturas (categoria = 'Pinturas')
    cant_categorias_pintura=Producto.objects.filter(categoria__exact='2').count()

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'cant_clientes':cant_clientes,'cant_productos':cant_productos,
                 'total_categorias':total_categorias,'cant_categorias_pintura':cant_categorias_pintura}
                 
    )

#Permite implementar una vista de cliente basada en Clase.
class ClienteListView(generic.ListView):
    model = Cliente

class ProductoListView(generic.ListView):
    model = Producto

class CategoriaListView(generic.ListView):
    model = Categoria