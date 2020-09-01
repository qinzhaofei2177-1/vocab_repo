from django import forms

# form classes
class TestForm(forms.Form):
    ##CHOICES = [('1', 'First'), ('2', 'Second')]
    word = forms.CharField(label='word', widget=forms.HiddenInput, initial="")
    options = forms.CharField(label='options', widget=forms.HiddenInput, initial="")
    choice = forms.ChoiceField(label='choice', widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__()
        
        opt = []
        for key, value in kwargs.items():
            if key == 'wordItem':
                self.fields['word'].initial = value.BaseWord
                self.fields['choice'].label = value.BaseWord
            if key == 'optionItems':
                for val in value:
                    opt.append((val.id, val.Defn))
                    self.fields['options'].initial += "||" + str(val.id) + "#" + str(val.Defn)
                    self.fields['options'].initial = self.fields['options'].initial.strip('||')
            if key == 'word':
                self.fields['word'].initial = value
                self.fields['choice'].label = value
            if key == 'options':
                self.fields['options'].initial = value
                d = dict(x.split("#") for x in value.split("||"))
                for k, v in d.items():
                    opt.append((k, v))
        
        self.fields['choice'].choices = opt
        