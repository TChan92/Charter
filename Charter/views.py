from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def line(request):
    return render(request, 'line.html')


def about(request):
    return render(request, 'about.html')
