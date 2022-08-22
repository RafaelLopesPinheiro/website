from django import forms

from .models import Acompanhamentos, Product, Quentinha

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
        model = Quentinha
        fields = ['acompanhamentos']
        unit = forms.MultipleChoiceField(choices=fields, widget=forms.CheckboxSelectMultiple,)
        


CHOICES_ACOMP = [
    ('ARROZ_BRANCO','Arroz Branco'),
    ('MACARRAO', 'Macarrão'),
    ('FEIJAO_PRETO', 'Feijão Preto'),
]

class Acompanha_Form(forms.Form):
    acompanhamentos = forms.ChoiceField(choices=CHOICES_ACOMP, widget=forms.CheckboxSelectMultiple,)
    

