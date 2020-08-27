from django.shortcuts import render, redirect

# Create your views here.

def client_list(request):
    return render(request, 'client_list.html')

def home(request):
    return render(request, 'index.html')
