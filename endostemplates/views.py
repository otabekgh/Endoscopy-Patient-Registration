from django.shortcuts import render
from django.views import generic
from .models import Device

# Create your views here.

class IndexTemplateView(generic.ListView):
    template_name = 'device_list.html'

    def get_queryset(self):
        return Device.objects.all()