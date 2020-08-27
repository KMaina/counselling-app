from django.shortcuts import render, redirect

#Create your views here.
def home(request):
    return render(request, 'index.html')

def counsel(request):
    return render(request, 'counsellors_list.html')