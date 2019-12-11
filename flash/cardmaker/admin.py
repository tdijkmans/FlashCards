from django.contrib import admin

# Register your models here.
from .models import Student, Stack, Card

class StudentAdmin(admin.ModelAdmin):
    fields = ['full_name']


class StackAdmin(admin.ModelAdmin):
    fields = ['subject', 'student']


class CardAdmin(admin.ModelAdmin):
    fields = ['question', 'answer', 'subject', 'student']



admin.site.register(Student, StudentAdmin)
admin.site.register(Stack, StackAdmin)
admin.site.register(Card, CardAdmin)
