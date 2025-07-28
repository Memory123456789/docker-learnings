# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
        path("", views.welcome, name="welcome"),
        path('info/', views.show_time_ip),
path("", views.index, name="index"),
path('counter/', views.counter_view)


]

