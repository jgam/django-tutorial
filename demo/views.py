# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Car

from .serializers import CarSerializer
from rest_framework import viewsets

# Create your views here.
class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

class Another(View):
    cars = Car.objects.all()#get all the cars
    output = f"we have {len(cars)} cars"
    def get(self, request):
        return HttpResponse(self.output)

def first(request):
    return HttpResponse('First message from views')

def second(request):
    return render(request, 'first_temp.html')