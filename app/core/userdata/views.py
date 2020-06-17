from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import reverse
# Create your views here.

class NosotrosPageView(TemplateView):

    template_name = "nosotros.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'titulous':'Acerca de Nosotras','subti':'ADSI','nomEstu1':'Stefanía Giraldo Monsalve','nomEstu2':'Daniela Zapata Gutierrez','nomEstu3':'Karen Vásquez Hernández','parr1':'Se encarga de desarrollar el sistema operativo de coinsa y de la realización de pruebas de calidad al codigo varias veces para garantizar su eficiencia.','parr2':'Se encarga de la administración de la base de datos y que todo fluya correctamente.','parr3':'Se encarga de diseñar la arquitectura del proyecto, se asegura que todos los requisitos propuestos sean cumplidos en el equipo de trabajo.'})

        