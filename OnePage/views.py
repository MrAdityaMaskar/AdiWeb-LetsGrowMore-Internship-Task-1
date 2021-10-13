from django.shortcuts import render
from .models import Contact
# Create your views here.


def contact(request):
    context = {'success': False}
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        ins = Contact(name=name, email=email, subject=subject, message=message)
        ins.save()
        context = {'success': True}
    return render(request, 'index.html', context)
