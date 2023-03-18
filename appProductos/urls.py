from django.urls import path ,  include

from .views import *

urlpatterns = [
    path('categorias/', verCategorias, name='Categorias'),
    path('productos/<str:idCategoria>', verProductosCategoria, name='Productos'),
    path('producto/<str:idProducto>', verProducto, name='un_Producto')
]
