from django.shortcuts import render
from django.http import HttpResponse

def start(request):
    return render(request, 'Start.html')
def hobby(request):
    return render(request, 'hobby.html')
# Create your views here.
def project(request):
    return render(request,'Projects.html')
def progress(request):
    return render(request, 'progress.html')
