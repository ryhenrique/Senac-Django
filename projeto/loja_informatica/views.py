from django.shortcuts import render
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all() # Busca todos os produtos
    return render(request, 'loja_informatica/lista_produtos.html' , {'produtos': produtos})