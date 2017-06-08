from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import *

# Create your views here.


def index(request):
    sonst = SonstigerArtikel.objects.all()
    bucher = Buch.objects.all()
    bluray = Bluray.objects.all()
    return render(request, 'index.html', {'sonstArtikel': sonst, 'bucher': bucher, 'bluray': bluray})


def view_artikel(request, artikel_id):
    a = get_object_or_404(Artikel, pk=artikel_id)
    f = Feedback.objects.filter(artikel=a)
    return render(request, 'view_artikel.html', {'artikel': a, 'feedback': f})


def impressum(request):
    return render(request, 'impressum.html')
