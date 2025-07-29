from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from datetime import datetime
import socket

def home(request):
    return render(request, "home.html")

def show_time_ip(request):
    ip = request.META.get('REMOTE_ADDR')
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Current Time: {time} | Your IP: {ip}")

def counter_view(request):
    count = request.session.get('count', 0)
    request.session['count'] = count + 1
    return HttpResponse(f"Visitor count: {count + 1}")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return HttpResponse(f"Thanks, {data['name']}! We received your message.")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})


