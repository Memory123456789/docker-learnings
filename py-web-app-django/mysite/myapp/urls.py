from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("info/", views.show_time_ip, name="info"),
    path("counter/", views.counter_view, name="counter"),
    path("contact/", views.contact, name="contact"),
]

