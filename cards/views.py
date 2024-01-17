from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CardsForm  # Convenção de nome para classes geralmente começa com letra maiúscula
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
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
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})