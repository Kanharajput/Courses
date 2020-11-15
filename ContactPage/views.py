from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def contact(request):
    if request.method == "POST":
        message = request.POST['message']
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']

        # sending mail
        send_mail(
                message_subject,                # subject
                message,                        # message
                message_email,                  # sending mail   
                ['kanharajput91@gmail.com']     # getting mail
                )
        return render(request,'contact.html', {'message_name':message_name})


    else:
        return render(request,'contact.html')  