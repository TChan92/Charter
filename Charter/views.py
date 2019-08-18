from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from data.data_controller import *


def index(request):
    return render(request, 'index.html')


def line(request):
    return render(request, 'line.html')


def pie(request):
    return render(request, 'pie.html')


def about(request):
    return render(request, 'about.html')


class NasaNeoList(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        data = get_nasa_neo()
        return Response(data)


class NasaNeoAverageDiameter(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        data = get_nasa_neo()

        data = get_neo_estimated_diameter(data)
        return Response(data)
