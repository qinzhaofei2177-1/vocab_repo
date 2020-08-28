from django import forms


class TestForm(forms.Form):
    CHOICES = [('1', 'First'), ('2', 'Second')]
    option = forms.ChoiceField(label='Word', widget=forms.RadioSelect, choices=CHOICES)