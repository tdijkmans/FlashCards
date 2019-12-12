from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_cards, name="show_all"),
    path('new/', views.new_card, name="new_card"),
    path('deleteCard/<int:card_id>/', views.delete_card, name="delete_card"),

]
