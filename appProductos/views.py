from django.shortcuts import render
from . import models



# Create your views here.
def verCategorias(request): 
    #Consulatar datos
    listaCategorias = models.Categoria.objects.all()
    #Enviar datos a la vista
    context =  { 'listaCategorias' : listaCategorias }
    
    return render(request, 'productos/categorias.html',context)



def verProductosCategoria (request,idCategoria):
    
    #Consularta de categorias
    idCat = int(idCategoria)
    
    nombreCat = models.Categoria.objects.get(id=idCat)
    
    
def verProducto (request,idProd,msj=None):
    idProd = int(idProd)
    regProducto = models.Producto.objects.get(id=idProd)
    
    context =  { 'regProducto' : regProducto,
                'titulo' : 'Detalles de' + str(regProducto.nombre),
                } 
    if msj:
        context['msj'] = msj
        
    return render(request, 'productos/producto.html',context)