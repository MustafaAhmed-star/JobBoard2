from django.shortcuts import render

from me import settings
from . models import Info
from django.core.mail import send_mail


# Create your views here.


def send_message(request):
    myinfo = Info.objects.last()

    if request.method =='POST':
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']

        send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
 
        )
        
    return render(request, 'contact/contact.html',{'myinfo':myinfo})