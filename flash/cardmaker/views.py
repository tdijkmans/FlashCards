from django.shortcuts import render
from cardmaker.models import Card, Stack, Student
from cardmaker.forms import CardForm
from django.shortcuts import redirect

# Create your views here.
def show_all_cards(request):
    c_list = Card.objects.all()
    context = {'list_of_cards' : c_list}
    return render(request, 'show_all_cards.html', context)

def new_card(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.save()
            return redirect('show_all')
    else:
            form = CardForm()
    return render(request, 'make_card.html', {'cardform':form})
