from django.urls import path
from . import views
from .views import DeckCreate


# app_name = 'cardmaker'

urlpatterns = [
    path('', views.show_all_decks, name='all_decks'),
    path('card/all', views.show_all_cards, name='all_cards'),
    path('card/delete/<int:card_id>/', views.delete_card, name="delete_card"),
    path('deck/all', views.show_all_decks, name='all_decks'),
    path('deck/delete/<int:deck_id>/', views.delete_deck, name="delete_deck"),
    path('deck/create/', views.DeckCreate.as_view(), name='create_deck'),
    path('deck/<deck_id>/', views.create_cards, name='create_cards'),
    path('deck/show/<int:deck_id>/', views.show_deck, name="show_deck"),
    path('deck/rehearse/<int:deck_id>/', views.rehearse_deck, name="rehearse_deck"),
    path('deck/save/<int:deck_id>/', views.save_for_study, name="save_for_study"),
    path('studyset/', views.show_my_studyset, name='show_my_studyset'),
    path('studyset/remove/<int:studentdeck_id>/',views.remove_from_studyset, name= 'remove_from_studyset'),
    path('deck/leitner/<int:deck_id>', views.leitner, name='leitner')

]
