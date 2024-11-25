from django import forms 
from produtos.models import Categoria, Produto 

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']
        labels = {
            'nome': 'Nome da Categoria',
            'descricao': 'Descrição da Categoria',
        }

class ProdutoForms(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'valor', 'descricao', 'quantidade', 'categoria']
        labels = {
            'nome': 'Nome do Produto',
            'valor': 'Valor unitário (R$)',
            'descricao': 'Descrição do Produto',
            'quantidade': 'Quantidade do Produto',
            'categoria': 'Categoria',
        }