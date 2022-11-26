from django.db import connection, models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

from django.db import models


class User(models.Model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30, null=True)
    airline = models.CharField(max_length=30, null=True)


class Flight(models.Model):
    flight_id = models.AutoField(primary_key=True, null=False)
    aircraft_id = models.CharField(max_length=30, null=True)
    company_airline = models.CharField(max_length=30, null=True)
    type_of_flight = models.CharField(max_length=30, null=True)
    terminal = models.CharField(max_length=30, null=True)
    time_at_gate = models.CharField(max_length=30, null=True)
    destination = models.CharField(max_length=30, null=True)
    duration = models.CharField(max_length=30, null=True)

