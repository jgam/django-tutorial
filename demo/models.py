# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Car(models.Model):
    STATUSES = (
        (0, 'Unknown'),
        (1, 'displayed'),
        (2, 'paid')
    )
    name = models.CharField(blank=False, null=True, unique=True, max_length = 36)
    description = models.TextField(max_length=256, blank=True, null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=20)
    bought = models.DateField(blank=True, null=True, default=None)#this can be a current Date
    is_used = models.BooleanField(default= False)
    image = models.ImageField(null=True, blank=True, upload_to='Carimage/')