# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Game(models.Model):
    location = models.CharField(max_length=250)  # could possibly be drop down list?
    datetime = models.DateTimeField  # HH/MM  DD/MM/YYYY
    price = models.FloatField(max_length=6)


class User(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=16)
    balance = models.FloatField(max_length=6)