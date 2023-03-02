from django.shortcuts import render
from django.contrib import messages


def index_view(request):


    context = {}
    return render(request, 'weather-app/index.html', context)

