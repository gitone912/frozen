from multiprocessing import context
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import ce
from django.contrib import messages

def index(request):
    context = {
        "variable": "this ia variable",
        "bokachoda": "this is bokachoda"
    }
    messages.success(request, 'Profile details updated, message sent data sent.')
    return render(request, 'index.html',context)


def about(request):
    return render(request, 'about.html')



def services(request):
    return render(request, 'services.html')



def contacts(request):
    if request.method == "POST":
        
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        contacts = ce(firstname=firstname,lastname=lastname,phone=phone,subject=subject)
        contacts.save()
        messages.success(request, 'Profile details updated, message sent data sent.')
    return render(request, 'contacts.html')



