from django.shortcuts import render
from categories.views import categories
from profiles.views import heading
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def contact(request):
    form = ContactForm(request.POST or None)
    confirm_message = None
    title = None

    if form.is_valid():
        name = form.cleaned_data['name']
        from_email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        to_email = [settings.EMAIL_HOST_USER]
        contact_message = '''
        From: %s
        Email: %s
        Message:
        %s''' %(name, from_email, message)
        subject = 'Message from My Blog'
        send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
        title = 'Thanks!'
        confirm_message = 'Thanks for the message. I will get back to you soon.'
        form = None

    context = {'heading': heading, 'categories': categories, 'title': title, 'confirm_message': confirm_message, 'form': form}
    return render(request, 'contact.html', context)

