from django.contrib import admin

#importamos las clase de los modelos
from .models import TipoDocu, CateProyecto, Proyectos, Documentos

# Register your models here.
# Registro del modelo de Tipo documento:
class TipoDocModel(admin.ModelAdmin):
    list_display = ["nombTipoDocu"]
    list_display_links =["nombTipoDocu"]
    list_filter = ["nombTipoDocu"]

    class Meta:
        model = TipoDocu

admin.site.register(TipoDocu)

# Registro del modelo de Categoria proyecto
class CategProyeModel(admin.ModelAdmin):
    list_display = ["arquitectura"]
    list_display_links =["arquitectura"]
    list_filter = ["arquitectura"]

    class Meta:
        model = CateProyecto

admin.site.register(CateProyecto)

# Registro del modelo  Categoria proyecto
class ProyectosModel(admin.ModelAdmin):
    list_display = ["nombProye"]
    list_display_links =["nombProye"]
    list_filter = ["nombProye"]

    class Meta:
        model = Proyectos

admin.site.register(Proyectos)

# Registro del modelo documentos
class DocumentosModel(admin.ModelAdmin):
    list_display = ["nombDocu"]
    list_display_links =["nombDocu"]
    list_filter = ["nombDocu"]

    class Meta:
        model = Documentos

admin.site.register(Documentos)
