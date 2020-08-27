from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'index.html')

def counsellorhome(request):
    return render(request, 'homecounsellor.html')