from django.shortcuts import render

def index(request):
    context = {
        
    }
    return render(request, 'notes/index.html', context)