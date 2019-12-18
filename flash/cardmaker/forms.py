from cardmaker.models import Card, Deck
from django.forms import ModelForm, Textarea, inlineformset_factory, TextInput
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView


# Create the form class.
class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ('question', 'answer', 'deck')
        # widgets = {'question':
        #                         Textarea(attrs={
        #                         'class':'form-control',
        #                         'placeholder': "Write your question or term here",
        #                         'autofocus': True}),
        #             'answer':
        #                         Textarea(attrs={
        #                         'class':'form-control',
        #                         'placeholder': "Write your answer or definition here",
        #                         'autofocus': True}),
        #             }


class DeckForm(ModelForm):
    class Meta:
        model = Deck
        fields = ('title', 'subject', 'description')
        widgets = {'title':
                                TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': "Title",
                                }),
                    'subject':
                                TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': "Subject e.g. Biology",
                                }),
                    'description':
                                Textarea(attrs={
                                'class': 'form-control',
                                'placeholder': "Description e.g. Molecular Biology of the Cell, chapter 5-7",
                                }),
                    }


CardFormSet = inlineformset_factory(
                Deck, Card,
                fields=('question','answer'),
                can_delete=False,
                extra=1,
                widgets={
                    'question': TextInput(attrs={"class":"form-control form-control-lg",
                                                    "placeholder":"Question",}),
                    'answer': TextInput(attrs={"class":"form-control",
                                                    "placeholder":"Answer"}),


                        }

                )
