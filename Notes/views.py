from django.shortcuts import render

def index(request):
    context = {
        
    }
    return render(request, 'notes/index.html', context)

def foryou(request):
    context = {
        
    }
    return render(request, 'notes/foryou.html', context)