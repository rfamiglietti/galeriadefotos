from django.shortcuts import render, get_object_or_404
from .models import Fotografia

# Create your views here.

def index(request):
    fotografias = Fotografia.objects.order_by("data_foto").filter(publicada=True)
    return render(request, 'fotos/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'fotos/imagem.html', {"fotografia": fotografia})