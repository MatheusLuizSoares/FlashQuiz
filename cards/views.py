from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CardsForm  # Convenção de nome para classes geralmente começa com letra maiúscula
from .models import Cards

class CardListView(ListView):
    model = Cards
    template_name = 'cards/list.html'
    context_object_name = 'cards'

class CardDetailView(DetailView):
    model = Cards
    template_name = 'cards/detail.html'
    context_object_name = 'card'  # Nome mais apropriado para o objeto individual

class CardCreateView(CreateView):
    model = Cards
    form_class = CardsForm
    template_name = 'cards/create.html'
    success_url = reverse_lazy('card-list')  # Corrigido o nome da URL reversa

class CardUpdateView(UpdateView):
    model = Cards
    form_class = CardsForm
    template_name = 'cards/update.html'
    success_url = reverse_lazy('card-list')  # Corrigido o nome da URL reversa

class CardDeleteView(DeleteView):
    model = Cards
    template_name = 'cards/delete.html'
    success_url = reverse_lazy('card-list')  # Corrigido o nome da URL reversa
