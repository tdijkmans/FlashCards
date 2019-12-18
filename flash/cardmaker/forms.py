from cardmaker.models import Card, Deck
from django.forms import ModelForm, Textarea, inlineformset_factory, TextInput
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView


# Create the form class.
class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ('question', 'answer', 'deck')
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


class DeckForm(ModelForm):
    class Meta:
        model = Deck
        fields = ('title', 'subject')
        widgets = {'title':
                                TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': "Title",
                                }),
                    'subject':
                                TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': "Subject e.g. biology",
                                }),
                    }
