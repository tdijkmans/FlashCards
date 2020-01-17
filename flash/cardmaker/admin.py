from django.contrib import admin

# Register your models here.
from .models import Deck, Card, LeitnerBox


class DeckAdmin(admin.ModelAdmin):
    fields = ['title', 'subject', 'creator', 'description', 'students']


class CardAdmin(admin.ModelAdmin):
    fields = ['question', 'answer', 'deck']

class LeitnerAdmin(admin.ModelAdmin):
    fields = ['title', 'proficiency_level', 'owner', "cards"]


admin.site.register(Deck, DeckAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(LeitnerBox, LeitnerAdmin)
