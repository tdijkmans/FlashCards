from django.urls import path
from . import views
from .views import StackCreate


# app_name = 'cardmaker'

urlpatterns = [
    path('', views.show_all_cards, name="all_cards"),
    path('stack/all', views.show_all_stacks, name='all_stacks'),
    path('stack/delete/<int:stack_id>/', views.delete_stack, name="delete_stack"),
    path('stack/create/', views.StackCreate.as_view(), name='create_stack'),
    path('stack/<stack_id>/', views.create_cards, name='create_cards'),

    path('card/delete/<int:card_id>/', views.delete_card, name="delete_card"),


]
