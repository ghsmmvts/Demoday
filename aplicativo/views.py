from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'base.html')

def pontodecoletas(request):
    return render(request, 'pontodecoletas.html')

def resultados(request):
    return render(request, 'resultados.html')

def login(request):
    return render(request,'login.html')
