# fotos/views.py

from django.shortcuts import render, get_object_or_404
from .models import Fotografia
from django.db.models import Q

def index(request):
    fotografias = Fotografia.objects.order_by("data_foto").filter(publicada=True)
    return render(request, 'fotos/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'fotos/imagem.html', {'fotografia': fotografia})

def pesquisar(request):
    fotografias = Fotografia.objects.order_by("data_foto").filter(publicada=True)
    
    termo_de_busca = request.GET.get('buscar')
    
    if termo_de_busca:
        fotografias = fotografias.filter(
            Q(nome__icontains=termo_de_busca) | 
            Q(legenda__icontains=termo_de_busca) | 
            Q(categoria__icontains=termo_de_busca)
        ).order_by("data_foto")
            
    # Adicione o termo de busca ao contexto
    contexto = {
        "cards": fotografias,
        "termo_de_busca": termo_de_busca
    }
            
    return render(request, 'fotos/pesquisa.html', contexto)