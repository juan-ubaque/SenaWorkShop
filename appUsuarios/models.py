from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.
class MyAccountManager (BaseUserManager):
    def create_user(self,firts_name,last_name,email,username,password=None):
        if not email:
            raise ValueError('El usuario debe tener correo')
        if not username:
            raise ValueError('El usuario debe tener nombre de usuario')
        
        user = self.model(
            firts_name = firts_name,
            last_name = last_name,
            username = username,
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_suoeruser (self,firts_name,last_name,email,username,password):
        user = self.create_user(
            firts_name = firts_name,
            last_name = last_name,
            username = username,
            email = self.normalize_email(email),
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Usuario (AbstractBaseUser):
    ROLES = (
        ('admin','Administrador'),
        ('user','Usuario'),
    )
    firts_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(verbose_name='email',max_length=60,unique=True)
    rol = models.CharField(max_length=50,choices=ROLES,default='user')

    #Atributos 
    date_joined = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firts_name','last_name','username']

    objects = MyAccountManager()

    def __str__(self):
        return '{} {}'.format(self.firts_name,self.last_name)
    
    def has_perm (self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms (self,add_label):
        return True
    
    class Meta:
        verbose_name_plural = 'Usuarios'