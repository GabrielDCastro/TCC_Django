from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def contato(request):
    return render(request, 'home/contato.html')

def perfil(request):
    return render(request, 'home/perfil.html')

def login(request):
    return render(request, 'home/login.html')

def registrar(request):
    return render(request, 'home/registrar.html')
