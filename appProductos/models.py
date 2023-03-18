from django.db import models

from appUsuarios.models import Usuario


# Create your models here.
class Categoria(models.Model):
    descripCategoria = models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.descripCategoria
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias de  Productos'
        #ordering = ['descripCategoria']


class Producto(models.Model):
    nombre = models.CharField(max_length=100,null=False)
    decripcion = models.CharField(max_length=300,null=False)
    precioUnitario = models.DecimalField(max_digits=8,decimal_places=2)
    unidad = models.CharField(max_length=10,null=False)
    existencia = models.IntegerField(null=False)
    imgGrande = models.ImageField(upload_to='productos',null=False)
    imgPeque = models.ImageField(upload_to='iconos',null=False)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        #ordering = ['descripProducto']
        


class Carro (models.Model):
    ESTADO_PROD = (
        ('activo','activo'),
        ('comprado','comprado'),
        ('anulado','anulado'),
    )
    usuario =models.ForeignKey(Usuario,on_delete=models.CASCADE, null=False)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE, null=False)
    cantidad  = models.IntegerField(null=False)
    precioUnitario = models.DecimalField(max_digits=8,decimal_places=2)
    estado = models.CharField(max_length=20,choices=ESTADO_PROD,default='activo')
    fechaCompra = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
        #ordering = ['descripProducto']