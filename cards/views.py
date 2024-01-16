from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import cardsForm
from .models import cards
class cardlistView(ListView):
  model=cards
  template_name='cards/list.html'
  context_object_name='cards'
class cardDetailView(DetailView):
 model=cards
 template_name='cards/detail.html'
 context_object_name='cards'
class cardCreateView(CreateView):
   model=cards
   form_class=cardsForm
   template_name='cards/create.html'
   success_url='/cards'
class cardsUPdateView(UpdateView):
  model=cards
  form_class=cardsForm
  template_name='cards/update.html'
  success_url='cards'
class cardsDeleteView(DeleteView):
  model=cards
  template_name='cards.html'
  success_url=reverse_lazy('cardlist')
  
  
  
   