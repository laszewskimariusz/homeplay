from django.shortcuts import render

def index(request):
    
    
    return render(request, 'film/index.html', {})