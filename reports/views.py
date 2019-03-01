from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'base.html', {})