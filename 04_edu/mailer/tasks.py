from celery import task
from django.core.mail import send_mail
from .models import Message

@task
def message_created(message):
    # message = Message.objects.get(id=message_id)
    subject = f'message nr. {message.id}'
    text = f'You have successfully placed an message.' \
              f'Your message ID is {message.id}.'
    mail_sent = send_mail(subject,
                          text,
                          'admin@edu.com',
                          [message.email])
    return mail_sent