"""proposal_login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from roles import views

urlpatterns = [
    path('register', views.register_user, name="register"),
    path('login', views.login, name="login"),
    path('edit_flight', views.edit_flight_timings, name="login"),
    # path('register', views.register_user, name="register"),
    # path('all_flights', views.all_flights, name="all_flights"),

]
