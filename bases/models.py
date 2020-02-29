from django.db import models

#Importamos el modelo de usuario
from django.contrib.auth.models import User

# Create your models here.
# En esta modelo van a estar los comapos que van a tener todos los modelos en comun
class ClaseModelo(models.Model):
    estado = models.BooleanField('Estado', default=True)
    # Automatica mente se pone la fecha cuando se crea con la propiedad 'auto_now_add'
    fc = models.DateTimeField('Fecha De Creación', auto_now_add=True)
    # esta fecha se modifica cada vez que se realice una accion 'auto_now'
    fm = models.DateTimeField('Fecha de Modificacion', auto_now=True)
    # Llave foranea que se optiene del usuario uno (Usuario) a muchos (Modelo)
    uc = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = "Usuario Crea")
    um = models.IntegerField('Usuario Modifica', blank=True, null=True)

    #Se crea esta clase para que no tenga encuenta este modelo a la hora de la migracion
    class Meta:
        abstract = True
