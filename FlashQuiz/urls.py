from django.contrib import admin
from django.urls import path
from cards.views import CardListView, CardCreateView, CardUpdateView, CardDeleteView, CardCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CardListView.as_view(), name='card-list'),  # Adicionei um nome à sua view
    path('card/create/', CardCreateView.as_view(), name='card-create'),
    path('card/update/<int:pk>/', CardUpdateView.as_view(), name='card-update'),  # Adicionei um parâmetro para o ID do objeto
    path('card/delete/<int:pk>/', CardDeleteView.as_view(), name='card-delete'),  # Adicionei um parâmetro para o ID do objeto
    path('card/complete/<int:pk>/', CardCompleteView.as_view(), name='card-complete'),  # Adicionei um parâmetro para o ID do objeto
]
