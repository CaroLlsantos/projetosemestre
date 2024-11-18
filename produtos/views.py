from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Categoria, Produto
from django.contrib.auth.mixins import LoginRequiredMixin
from produtos.forms import CategoriaForm, ProdutoForms

class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'categoria_list.html'

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria_form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria_form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria_list')

class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'produto_list.html'

class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    form_class = ProdutoForms
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produto_list')

class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoForms
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produto_list')

class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'produto_confirm_delete.html'
    success_url = reverse_lazy('produto_list')

