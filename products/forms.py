from django import forms

from .models import Acompanhamentos, Product, Quentinha, Order

        

class QuentinhaForm(forms.ModelForm):
    class Meta:
        model = Quentinha
        fields = ['acompanhamentos']
        form_class = forms.MultipleChoiceField(choices=fields, widget=forms.CheckboxSelectMultiple)

    # def clean_titlte(self, *args, **kwargs):
    #     title = self.cleaned_data.get('title')        


CHOICES_ACOMP = [
    ('ARROZ_BRANCO','Arroz Branco'),
    ('MACARRAO', 'Macarrão'),
    ('FEIJAO_PRETO', 'Feijão Preto'),
]

class Acompanha_Form(forms.Form):
    acompanhamentos = forms.MultipleChoiceField(choices=CHOICES_ACOMP, widget=forms.CheckboxSelectMultiple,)
    

