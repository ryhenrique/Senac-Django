from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'loja_informatica/lista_produtos.html', {'produtos': produtos})

def inserir_produto(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        preco = request.POST['preco']
        estoque = request.POST['estoque']
        Produto.objects.create(nome=nome, descricao=descricao, preco=preco, estoque=estoque)
        return redirect('lista_produtos')

def alterar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        produto.nome = request.POST['nome']
        produto.descricao = request.POST['descricao']
        produto.preco = request.POST['preco']
        produto.estoque = request.POST['estoque']
        produto.save()
        return redirect('lista_produtos')
    return render(request, 'loja_informatica/alterar_produto.html', {'produto': produto})

def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    produto.delete()
    return redirect('lista_produtos')