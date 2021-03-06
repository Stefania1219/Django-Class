from django.contrib import admin
#importamos las clase de los modelos
from .models import Roles, DatosUser, HabilUser, DetaRoles, Rates

# Register your models here.
# Registro del modelo de Roles:
class RoleModel(admin.ModelAdmin):
    list_display = ["RoleName"]
    list_display_links =["RoleName"]
    list_filter = ["RoleName"]

    class Meta:
        model = Roles

admin.site.register(Roles)

# Registro del modelo de DatoUser:
class DatosUserModel(admin.ModelAdmin):
    list_filter = ["nombUser", "apelUser"]
    list_display_links = ["nombUser", "apelUser"]

    class Meta:
        model = DatosUser
        
admin.site.register(DatosUser)

# Registro del modelo de Habilidades:
class HabilUserModel(admin.ModelAdmin):
    list_filter = ["NombHabil"]

    class Meta:
        model = HabilUser

admin.site.register(HabilUser)

# Registro del modelo Detalle de los roles:
class DetaRolesModel(admin.ModelAdmin):
    list_filter = ["estaRol"]

    class Meta:
        model = DetaRoles

admin.site.register(DetaRoles)

# Registro del modelo Detalle de los roles:
class RatesModel(admin.ModelAdmin):
    list_filter = ["pcrHabil"]

    class Meta:
        model = Rates    
admin.site.register(Rates)
