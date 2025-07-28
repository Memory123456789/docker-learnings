from django.shortcuts import render

# Create your views here.

# myapp/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("🌟 Hello, Mr. Kurella Chandra Sekhar! This is your own customised Django-powered web app.")

def welcome(request):
    return HttpResponse("<h1>Welcome to Krishna's Page 🚀</h1>")

from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse("Thanks for your message!")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

from datetime import datetime

def show_time_ip(request):
    ip = request.META.get('REMOTE_ADDR')
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Your IP: {ip}<br>Current time: {time}")
def counter_view(request):
    count = request.session.get('count', 0)
    count += 1
    request.session['count'] = count
    return HttpResponse(f"Visit count: {count}")

