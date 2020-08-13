from django.shortcuts import render
from .models import Contact, AllNotes


# Create your views here.
def index(request):
    return render(request, 'notes/index.html')


def about(request):
    return render(request, 'notes/about.html')


def viewNotes(request):
    return render(request, 'notes/viewNotes.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'notes/contact.html')
