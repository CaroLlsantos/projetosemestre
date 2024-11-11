from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import MovimentacaoForm
from .models import Movimentacao

class MovimentacaoListView(ListView):
    model = Movimentacao
    template_name = 'movimentacao_list.html'

class MovimentacaoCreateView(CreateView):
    model = Movimentacao 
    form_class = MovimentacaoForm
    template_name = 'movimentacao_form.html'
    success_url = reverse_lazy('movimentacao_list')

class MovimentacaoUpdateView(UpdateView):
    model = Movimentacao
    form_class = MovimentacaoForm
    template_name = 'movimentacao_form.html'
    success_urls = reverse_lazy('movimentacao_list')

class MovimentacaoDeleteView(DeleteView):
    model = Movimentacao
    template_name = 'movimentacao_confirm_delete.html'
    success_urls = reverse_lazy('movimentacao_list')