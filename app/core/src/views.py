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