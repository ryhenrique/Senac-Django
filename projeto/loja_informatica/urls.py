from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('inserir/', views.inserir_produto, name='inserir_produto'),
    path('alterar/<int:produto_id>/', views.alterar_produto, name='alterar_produto'),
    path('deletar/<int:produto_id>/', views.deletar_produto, name='deletar_produto'),
]
