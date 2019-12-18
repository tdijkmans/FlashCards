from django.urls import path
from . import views
from .views import DeckCreate


# app_name = 'cardmaker'

urlpatterns = [
    path('', views.show_all_cards, name="all_cards"),
    path('deck/all', views.show_all_decks, name='all_decks'),
    path('deck/delete/<int:deck_id>/', views.delete_deck, name="delete_deck"),
    path('deck/create/', views.DeckCreate.as_view(), name='create_deck'),
    path('deck/<deck_id>/', views.create_cards, name='create_cards'),

    path('card/delete/<int:card_id>/', views.delete_card, name="delete_card"),


]
