from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def fruits(request):
    return render(request, 'fruit.html')

def contact(request):  
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')      