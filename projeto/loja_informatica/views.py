from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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

def cadastro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # Redireciona para a URL que você quiser
    else:
        form = UserCreationForm()
    return render(request, 'loja_informatica/cadastro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Ajuste para a URL que quiser
    else:
        form = AuthenticationForm()
    return render(request, 'loja_informatica/login.html', {'form': form})