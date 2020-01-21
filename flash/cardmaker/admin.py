from django.contrib import admin

# Register your models here.
from .models import Deck, Card, StudySet, LeitnerBox, ScoreBoard, StudentDeck


class DeckAdmin(admin.ModelAdmin):
    fields = ['title', 'subject', 'creator', 'description']


class CardAdmin(admin.ModelAdmin):
    fields = ['question', 'answer', 'deck']


class StudySetAdmin(admin.ModelAdmin):
    fields = ['student']

class StudentDeckAdmin(admin.ModelAdmin):
    fields = ['studyset', 'student', 'deck']


class LeitnerBoxAdmin(admin.ModelAdmin):
    fields = ['frequency']


class ScoreBoardAdmin(admin.ModelAdmin):
    fields = ['student', 'card', 'box', 'updated', 'leitner_date']


admin.site.register(Deck, DeckAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(StudySet, StudySetAdmin)
admin.site.register(ScoreBoard, ScoreBoardAdmin)
admin.site.register(LeitnerBox, LeitnerBoxAdmin)
admin.site.register(StudentDeck, StudentDeckAdmin)
