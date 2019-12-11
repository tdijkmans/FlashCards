from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.show_all_cards, name="show_all"),
    path('new/', views.new_card, name="new_card"),

]
