from django import forms

from .models import Acompanhamentos, Quentinha

class Quentinha_form(forms.ModelForm):
    class Meta:
        model = Quentinha
        fields = [
            'title',
            'description',
            'price','acompanhamentos',
        ]

    # def clean_titlte(self, *args, **kwargs):
    #     title = self.cleaned_data.get('title')

        

class QuentinhaForm(forms.ModelForm):
    class Meta:
        model = Acompanhamentos
        fields = ['acomp_choices']



CHOICES_ACOMP = [
    ('ARROZ_BRANCO','Arroz Branco'),
    ('MACARRAO', 'Macarrão'),
    ('FEIJAO_PRETO', 'Feijão Preto'),
]

class Acompanha_Form(forms.Form):
    acompanhamentos = forms.MultipleChoiceField(choices=CHOICES_ACOMP, widget=forms.CheckboxSelectMultiple,)
    

