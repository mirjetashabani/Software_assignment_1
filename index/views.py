from django.shortcuts import render
from django.http import *

def front_page(request):
    return render(request, "index.html")