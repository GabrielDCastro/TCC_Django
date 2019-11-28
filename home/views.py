from django.shortcuts import render
from .forms import Contact

def home(request):
    return render(request, 'home/home.html')

def contato(request):
    return render(request, 'home/contato.html')

def perfil(request):
    return render(request, 'home/perfil.html')

def login(request):
    return render(request, 'home/Login.html')

def registrar(request):
    return render(request, 'home/registrar.html')

def duvidas(requests):
    context = {}
    if requests.method == 'POST':
        form = Contact(requests.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_email()
            form = Contact()
    else:
        form = Contact()
    context['form'] = form
    return render(requests, 'home/duvidas.html', context)
