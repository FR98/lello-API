from django.core.mail import send_mail
from django.template.loader import render_to_string

def enviar_email(to, message):
    send_mail(
        'Hello from Lello',
        message,
        'lellodjango@gmail.com',
        to,
        fail_silently = False,
        html_message = render_to_string(
            'send/index.html',
            {
                'message': message
            }
        )
    )
    print("Email enviado con exito!")
