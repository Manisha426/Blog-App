from django.shortcuts import render
from . import views

def profile(request):
    return render(request, 'employee/profile.html')

# Create your views here.
