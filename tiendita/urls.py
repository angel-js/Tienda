from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.ClienteListView.as_view(), name='clientes'),
    path('productos/', views.ProductoListView.as_view(), name='productos'),
    path('categoria/', views.CategoriaListView.as_view(), name='categoria'),
]
