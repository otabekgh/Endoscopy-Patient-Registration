from django.shortcuts import render
# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'base.html', {})

def templates_view(request):
    return render(request, 'templates.html', {})