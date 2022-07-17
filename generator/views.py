from django.shortcuts import render
from django.http import HttpResponse
import string
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    thepassword = ''
    if request.GET.get('uppercase'):
        lower += upper
    if request.GET.get('special'):
        lower += '!@#$%^&*'
    if request.GET.get('numbers'):
            lower += digits

    length = int(request.GET.get('length'))
    for i in range(length):
        thepassword += random.choice(lower)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')
