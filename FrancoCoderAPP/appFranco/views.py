from django.shortcuts import render
from appFranco.models import*
# Create your views here.
def crear_familia(request):
    nombre=familia.objects.all()
    return render(request, "index.html", {'nombre':nombre})
