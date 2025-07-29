from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
import requests

visitor_count = 0  # Basic visitor counter (in-memory, resets on server restart)

def dashboard(request: HttpRequest):
    global visitor_count
    visitor_count += 1

    # Get client IP
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')

    # API data (example with random cat fact)
    cat_fact = None
    try:
        response = requests.get("https://catfact.ninja/fact")
        if response.status_code == 200:
            cat_fact = response.json().get("fact")
    except:
        cat_fact = "Could not fetch cat fact."

    context = {
        "current_time": datetime.now(),
        "client_ip": ip,
        "visitor_count": visitor_count,
        "cat_fact": cat_fact,
    }

    return render(request, "myapp/dashboard.html", context)
