from cardmaker.models import Card, Stack, Student
from django.forms import ModelForm, Textarea

# Create the form class.
class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ('question', 'answer', 'student', 'stack')
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
