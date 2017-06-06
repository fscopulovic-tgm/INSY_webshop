from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import *

# Create your views here.


def index(request):
    ls = Land.objects.all()
    a = Artikel.objects.all()
    return render(request, 'index.html', {'countries': ls, 'artikel': a})


def view_artikel(request, artikel_id):
    a = get_object_or_404(Artikel, pk=artikel_id)
    return render(request, 'view_artikel.html', {'artikel': a})


def impressum(request):
    return render(request, 'impressum.html')
