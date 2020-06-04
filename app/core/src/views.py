from django.views.generic.base import TemplateView
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Crea tus puntos de vista aquí.

class HomePageView(TemplateView):

    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'tituloIni':'Los saluda Stefania Giraldo.', 'titulo2':'Clases de python.'})

class NosotrosPageView(TemplateView):

    template_name = "nosotros.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'titulous':'Acerca de Nosotras','subti':'ADSI','nomEstu1':'Stefanía Giraldo Monsalve','nomEstu2':'Daniela Zapata Gutierrez','nomEstu3':'Karen Vásquez Hernández','parr1':'Se encarga de desarrollar el sistema operativo de coinsa y de la realización de pruebas de calidad al codigo varias veces para garantizar su eficiencia.','parr2':'Se encarga de la administración de la base de datos y que todo fluya correctamente.','parr3':'Se encarga de diseñar la arquitectura del proyecto, se asegura que todos los requisitos propuestos sean cumplidos en el equipo de trabajo.'})

# Vista basada en función:
def contacto(request):
    formContact = ContactForm(data=request.POST)

    # Validar que el formulario tenga una petición post:
    if request.method == "POST":
        # Reconfiguramos formcotact con los datos que hemos enviado, es decir rellenamos la plantilla del formulario:
        formContact = ContactForm(data=request.POST)
        if formContact.is_valid():
            tipomsj = request.POST.get('tipomsj','')
            usuario = request.POST.get('usuario','')
            correo = request.POST.get('correo','')
            mensaje = request.POST.get('mensaje','')

            # Creamos el objeto con las variables del formulario:
            email = EmailMessage(
                "COINSA: tienes un nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\nTipo de Mensaje:{}\n{}".format(usuario, correo, tipomsj, mensaje),
                "no-contestar@inbox.mailtrap.io",
                ["stefania1219@hotmail.com"],
                reply_to=[correo]
            )
             # Enviamos el correo:
            try:
                email.send()
                # Se envia el correo:
                return redirect(reverse('contacto')+"?ok")
            except:
                # No se ha enviado el correo:
                return redirect(reverse('contacto')+"?fail")
    
    
    return render(request, 'contacto.html', {'formulario':formContact})