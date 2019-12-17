from cardmaker.models import Card, Stack, Student
from django.forms import ModelForm, Textarea, inlineformset_factory, TextInput
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView


# Create the form class.
class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ('question', 'answer', 'stack')
        widgets = {'question':
                                Textarea(attrs={
                                'label':'hi!',
                                'cols':33,
                                'rows':7,
                                'placeholder': "Write your question or term here",
                                'autofocus': True}),
                    'answer':
                                Textarea(attrs={
                                'cols':33,
                                'rows':7,
                                'placeholder': "Write your answer or definition here",
                                'autofocus': True}),
                    }


class StackForm(ModelForm):
    class Meta:
        model = Stack
        fields = ('title', 'subject')
        widgets = {'title':
                                TextInput(attrs={
                                'placeholder': "Title",
                                }),
                    'subject':
                                TextInput(attrs={
                                'placeholder': "Subject e.g. biology",
                                }),
                    }
