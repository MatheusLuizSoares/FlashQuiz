from django.contrib import admin
from django.urls import path
from cards.views import CardListView, CardCreateView, CardUpdateView, CardDeleteView, CardCompleteView
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CardListView.as_view(), name='card-list'),
    path('card/create/', CardCreateView.as_view(), name='card-create'),
    path('card/update/<int:pk>/', CardUpdateView.as_view(), name='card-update'),
    path('card/delete/<int:pk>/', CardDeleteView.as_view(), name='card-delete'),
  
    path('card/complete/<int:pk>/', CardCompleteView.as_view(), name='card-complete'),
    path('accounts/', include('django.contrib.auth.urls')),
    ]