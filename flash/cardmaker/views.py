from django.shortcuts import render
from cardmaker.models import Card, Deck
from cardmaker.forms import CardForm, DeckForm, CardFormSet
from django.shortcuts import redirect

from django.views.generic.edit import CreateView


# Create your views here.
def show_all_cards(request):
    c_list = Card.objects.all()
    context = {'list_of_cards' : c_list}
    return render(request, 'show_all_cards.html', context)


def delete_card(request, card_id):
    card_to_delete = Card.objects.get(id=card_id)
    card_to_delete.delete()
    return redirect('all_cards')


def show_all_decks(request):
    d_list = Deck.objects.all()
    context = {'list_of_decks': d_list}
    return render(request, 'show_all_decks.html', context)


def delete_deck(request, deck_id):
    deck_to_delete = Deck.objects.get(id=deck_id)
    deck_to_delete.delete()
    return redirect('all_decks')


class DeckCreate(CreateView):
    form_class = DeckForm
    model=Deck

    def form_valid(self, form):
        f = form.save(commit=False)
        f.creator = self.request.user
        f.save()
        return super().form_valid(form)


def create_cards(request, deck_id):
    deck = Deck.objects.get(pk=deck_id)

    if request.method == 'POST':
        formset = CardFormSet(request.POST, instance = deck)
        if formset.is_valid():
            formset.save()
            return redirect('create_cards', deck_id)

    formset = CardFormSet(instance=deck)
    return render(request, 'create_cards.html', {'formset':formset, 'deck': deck})


def show_deck(request, deck_id):
    deck = Deck.objects.get(pk=deck_id)
    c_list = Card.objects.filter(deck_id=deck)
    context = {'list_of_cards' : c_list, 'deck':deck}

    return render(request, 'show_deck.html', context)


# rehearsing the deck means 'a slidehow of flashcards', flipping cards when
# needed (showing question or answer side)
def rehearse_deck(request, deck_id):
    deck = Deck.objects.get(pk=deck_id)
    c_list = Card.objects.filter(deck_id=deck)
    context = {'list_of_cards' : c_list}

    return render(request, 'rehearse_deck.html', context)

def leitner_deck(request, deck_id):
    deck = Deck.objects.get(pk=deck_id)
    c_list = Card.objects.filter(deck_id=deck)
    context = {'list_of_cards' : c_list}

    return render(request, 'leitner_deck.html', context)
