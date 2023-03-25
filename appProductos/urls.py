from django.urls import path

from .views import *

urlpatterns = [
    path('categorias/', verCategorias, name='Categorias'),
    path('productos/<str:idCategoria>', verProductosCategoria, name='Productos'),
    path('producto/<str:idProducto>', verProducto, name='un_Producto'),

    #Carrito
    path('carrito/', verCarrito, name='verCarrito'),
    path('carrito/<str:idProd>', agregarCarrito, name='agregarCarrito'),
    path('carrito/eliminar/<str:idProd>', eliminarCarrito, name='eliminarCarrito'),
    path('cambiarCantidad/', cambiarCantidad),

    path('pagar/',pagarCarrito, name='pagar'),


]
