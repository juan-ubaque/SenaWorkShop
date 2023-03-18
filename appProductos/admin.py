from django.contrib import admin
from .models import *


#Registrando el modelo Producto  y Categoria de la app appProductos

#Mejorando la vista de los modelos en el admin
#--------------------------------------------
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','descripCategoria']

admin.site.register(Categoria,CategoriaAdmin)
    
#--------------------------------------------
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','decripcion','existencia']


admin.site.register(Producto,ProductoAdmin)

#--------------------------------------------
class CarroAdmin(admin.ModelAdmin):
    list_display = ['usuario','producto','cantidad','estado']

admin.site.register(Carro,CarroAdmin)
