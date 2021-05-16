from django.views.generic.edit import FormView
from django.shortcuts import render

from .tasks import message_created
from .forms import MessageForm

class ContactFormView(FormView):
    template_name = 'mailer/contacts.html'
    form_class = MessageForm
    success_url = '/'

    def form_valid(self, form):
        new_message = form.save()
        message_created(new_message)
        return super(ContactFormView, self).form_valid(form)
