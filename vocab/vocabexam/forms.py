from django import forms
from django.db.models import Max
from .models import Dictionary
import random

# Utility functions
def random_words(count=1):
    max_id = Dictionary.objects.all().aggregate(max_id=Max("id"))['max_id']
    word = None
    rand_word_list = []
    while len(rand_word_list) < count:
        while word==None:
            pk = random.randint(1, max_id)
            word = Dictionary.objects.get(pk=pk)
        else:
            rand_word_list.append(word)
            word = None

    return rand_word_list

def generate_options(word, totalOpt=4):
    pos = random.randint(0, totalOpt-1)
    options = random_words(totalOpt-1)
    options.insert(pos, word)
    return options

# form classes
class TestForm(forms.Form):
    ##CHOICES = [('1', 'First'), ('2', 'Second')]
    option = forms.ChoiceField(label='word', widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        w = random_words(1)[0]
        self.fields['option'].label = w.BaseWord
        ch = []
        options = generate_options(w, 4)
        for o in options:
            ch.append((o.id, o.Defn))
        self.fields['option'].choices = ch