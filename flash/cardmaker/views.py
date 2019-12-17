from django.shortcuts import render
from cardmaker.models import Card, Stack, Student
from cardmaker.forms import CardForm, StackForm
from django.shortcuts import redirect
from django.forms import modelformset_factory, inlineformset_factory
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


def show_all_stacks(request):
    s_list = Stack.objects.all()
    context = {'list_of_stacks': s_list}
    return render(request, 'show_all_stacks.html', context)


def delete_stack(request, stack_id):
    stack_to_delete = Stack.objects.get(id=stack_id)
    stack_to_delete.delete()
    return redirect('all_stacks')


class StackCreate(CreateView):
    form_class = StackForm
    model=Stack
    # fields = ['title', 'subject']

    def form_valid(self, form):
        f = form.save(commit=False)
        f.creator = self.request.user
        f.save()
        return super().form_valid(form)


def create_cards(request, stack_id):
    stack = Stack.objects.get(pk=stack_id)
    CardFormSet = inlineformset_factory(Stack, Card, fields=('question','answer'))

    if request.method == 'POST':
        formset = CardFormSet(request.POST, instance = stack)
        if formset.is_valid():
            formset.save()
            return redirect('create_cards', stack_id)

    formset = CardFormSet(instance=stack)
    return render(request, 'create_cards.html', {'formset':formset, 'stack':stack})
