from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from .genero import Generos

# Crea tus modelos aquí.
# Crear la estructura de la aplicación del modelo de datos:

# Modelo de la tabla Roles
class Roles(models.Model):
    RoleName = models.CharField(max_length = 50)

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "perfiles"

    # Función de selección:
    def __str__(self):
        return self.RoleName

# Crear los demás modelos para la aplicacion datos user (userdata):
# Modelo de la tabla DatosUser

class DatosUser(models.Model):
    idUser = models.CharField(max_length = 20, verbose_name= "Identificación")
    nombUser = models.CharField(max_length = 200, null=True, verbose_name= "Nombres")
    apelUser = models.CharField(max_length = 200, null=True, verbose_name= "Apellidos")
    profeUser = models.CharField(max_length = 100, null=True, verbose_name= "Profesión")
    fotoUser = models.ImageField(verbose_name= "Foto de perfil",  upload_to = "img/perfiles")
    teleUser = models.CharField(max_length = 20, verbose_name= "Número de Teléfono")
    geneUser = models.CharField(max_length = 20, choices = Generos, default = "Otro", verbose_name= "Género")
    adddata = models.DateTimeField(auto_now_add = True, null=True, auto_now = False, verbose_name= "Creado el")
    modifiat = models.DateTimeField(auto_now = True, null=True, verbose_name= "Modificado el")

    class Meta:
        verbose_name = "Datos de Usuario"
        verbose_name_plural = "Información"
        

    # Función de selección:
    def __str__(self):
        return self.nombUser

# Modelo de la tabla habilidades

class HabilUser(models.Model):
    NombHabil = models.CharField(max_length = 100)
    DescHabil = models.TextField(max_length = 2000, verbose_name = "Descripcion de la habilidad")

    class Meta:
        verbose_name = "Habilidades del Usuario"
        verbose_name_plural = "Competencias"

    #Función de selección:
    def __str__(self):
        return self.NombHabil

# Agregamos los modelos de detalle:

class DetaRoles(models.Model):
    idRoles = models.ForeignKey(Roles, on_delete = models.CASCADE, verbose_name = "Identificador de Rol")
    idUser = models.ForeignKey(DatosUser, on_delete = models.CASCADE)
    addUser = models.DateTimeField(auto_now_add = True, auto_now = False)
    udtUser = models.DateTimeField(auto_now = True)
    estaRol= models.CharField(max_length = 10)

    class Meta:
        verbose_name = "Roles de Usuario"
        verbose_name_plural = "Roles"

    #Función de selección:
    def __unicode__(self):
        return self.idRoles

# modelo de la tabla Rates:

class Rates(models.Model):
    idHabil = models.ForeignKey(HabilUser, on_delete = models.CASCADE)
    idUser = models.ForeignKey(DatosUser, on_delete = models.CASCADE)
    pcrHabil = models.DecimalField(max_digits = 2, decimal_places = 1)
    udtHabil = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = "Nivel de Habilidad"
        verbose_name_plural = "Niveles de usuario"

    #Función de selección:
    def __str__(self):
        return self.pcrHabil




