import json

from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render
from .models import Categoria, Producto

# Create your views here.
def verCategorias(request): 
    #Consulatar datos
    listaCategorias     = Categoria.objects.all()
    #Enviar datos a la vista
    context             = { 
                            'listaCategorias' : listaCategorias,
                            'titulo' : 'Categorias de Productos',}
    
    return render(request, 'productos/categorias.html',context)



def verProductosCategoria (request,idCategoria):
    
    #Consularta de categorias
    idCat           = int(idCategoria)
    
    nombreCat       = Categoria.objects.get(id=idCat)

    listaProductos  = Producto.objects.filter(categoria = idCat)

    context         = {
                        'listaProductos':listaProductos,
                        'titulo':'Productos de la categoria ' + str(nombreCat),
                        }
    return render(request, 'productos/productos.html',context)
    
    
def verProducto (request,idProducto,msj=None):
    idProd      = int(idProducto)
    regProducto = Producto.objects.get(id=idProd)
    
    context     =  { 
                    'producto' : regProducto,
                    'titulo' : 'Detalles de  ' + str(regProducto.nombre),
                    } 
    if msj:
        context['msj'] = msj
        
    return render(request, 'productos/producto.html',context)




def agregarCarrito (request,idProd):
    idProd      = int(idProd)

    regUsuario  = request.user

    #leer reg del producto
    existe      = Producto.objects.filter(id= idProd).exists()
    if existe:
        regProducto = Producto.objects.get(id=idProd)
        
        #si no existe
        existe = Carro.objects.filter(usuario=regUsuario,producto=regProducto).exists()
        if existe:
            #intancia de clase carro
            regCarro = Carro.objects.get(usuario=regUsuario,producto=regProducto,estado = 'activo')
            regCarro.cantidad += 1
        else:
            regCarro = Carro(   usuario         =regUsuario,
                                producto        =regProducto,
                                cantidad        =1,
                                precioUnitario  =regProducto.precioUnitario
                            )
            #Guardamos el registro
        regCarro.save()
        msj = 'Producto agregado al carrito'
    else:
        msj = 'Producto no disponible'
        
    return verProducto(request,idProd,msj)


def verCarrito (request):
    regUsuario  = request.user
    listaCarro  = Carro.objects.filter(usuario=regUsuario,estado='activo')
    context     = {
                    'listaCarro':listaCarro,
                    'titulo':'Carrito de compras',
                    }
    return render(request, 'productos/carrito.html',context)


def eliminarCarrito (request,idProd):
    #consultamos carro 
    regCarrito = Carro.objects.get(id=idProd)
    regCarrito.estado = 'anulado'

    regCarrito.save()
    return verCarrito(request)


def borrarProCarrito (request):
    if_ajax = request.META.get('HTTP_X_REQUEST_WITH')== 'XMLHttpRequest'

    if if_ajax:
        if request.method == 'POST':
            #Tomamos los datos de lado del cliente
            data = json.load(request)
            idProd = data.get('id')
            cantidad = int(data.get('cantidad'))
            if cantidad > 0 :
                regCarrito = Carro.objects.get(id=idProd)
                regCarrito.cantidad = cantidad
                regCarrito.save()
            regUsuario  = request.user
            listaCarro  = Carro.objects.filter(usuario=regUsuario,estado='activo')
            context     = {
                            'listaCarro':listaCarro,
                            'titulo':'Carrito de compras',
                            }
            return JsonResponse({
                'alarma' : 'no se pudo modificar...'},status=400
                                )
        else:
            return verCarrito(request)
        
def consultaCarrito(request):
    #get usuario
    regUsuario  = request.user
    #filtar productos de ese usuario en estado activo
    listaCarro  = Carro.objects.filter(usuario=regUsuario,estado='activo').values(
    'id',
    'cantidad',
    'valUnit',
    'producto__imgPeque',
    'producto__nombre',
    'producto__unidad',
    'producto__id')
    #renderizar
    listado = []
    subtotal= 0
    for prod in listaCarro:
        reg= {
            'id'        : prod['id'],
            'cantidad'  : prod['cantidad'],
            'valUnit'   : prod['valUnit'],
            'imgPeque'  : prod['producto__imgPeque'],
            'nombre'    : prod['producto__nombre'],
            'unidad'    : prod['producto__unidad'],
            'total'     : prod['valUnit'] * prod['cantidad'],
            'idProd'    : prod['producto__id'],
        }
        subtotal +=prod['valUnit']* prod['cantidad']



def cambiarCantidad(request):
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            #Tomamos los datos de lado del cliente
            data = json.load(request)
            idProd = data.get('id')
            cantidad = int(data.get('cantidad'))
            if cantidad > 0 :
                #lee el registro y lo modifica
                regCarrito = Carro.objects.get(id=idProd)
                regCarrito.cantidad = cantidad
                regCarrito.save()
            context = consultaCarrito(request)
            return JsonResponse(context)
        return JsonResponse({'alarma' : 'no se pudo modificar...'},status=400)
    else:
        return verCarrito(request)
    


def pagarCarrito(request):
    context = consultaCarrito(request)
    regUsuario = request.user
    nombreUsuario = str(regUsuario)
    context['nombre'] = nombreUsuario
    correo = regUsuario.email
    #--- MODULO PARA ENVIO DE CORREO
    mail_subject = 'Factura de compra'
    body = render_to_string('productos/html_email.html', context)
    to_email = [correo] #Lista con el o los correos de destino
    send_email = EmailMessage(mail_subject, body, to= to_email )
    send_email.content_subtype = 'html'
    send_email.send()

    #---FIN MODULO PARA ENVIO DE CORREO DE CONFIRMACION


    # sacar productos del carrito

    listaCarrito = Carro.objects.filter(usuario= regUsuario, estado= 'activo')
    for regCarro in listaCarrito:
        regCarro.estado = 'comprado'
        regCarro.save()
    #redireccionar
    return verCategorias(request)
