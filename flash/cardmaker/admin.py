from django.contrib import admin

# Register your models here.
from .models import Deck, Card


class DeckAdmin(admin.ModelAdmin):
    fields = ['title', 'subject', 'creator', 'description']


class CardAdmin(admin.ModelAdmin):
    fields = ['question', 'answer', 'deck']


admin.site.register(Deck, DeckAdmin)
admin.site.register(Card, CardAdmin)
