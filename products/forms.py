from xml.dom import ValidationErr
from django import forms
from cart.models import Order
from .models import Acompanhamentos, Extra, Quentinha

ACOMP_CHOICES = [
    ('ARROZ_BRANCO','Arroz Branco'),
    ('MACARRAO', 'Macarrão'),
    ('FEIJAO_PRETO', 'Feijão Preto'),
]        


class Book_form(forms.Form):
    acompanhamentos = forms.ModelMultipleChoiceField(
                        queryset=Acompanhamentos.objects.all(),
                        )#widget=forms.CheckboxSelectMultiple,)
    
    
    # class Meta:
    #     model = Quentinha
    #     # fields = ['acomp_choices', 'id']
    #     fields = ['acompanhamentos']
        


class Acompanha_Form(forms.ModelForm):
    acompanhamentos = forms.MultipleChoiceField(choices=ACOMP_CHOICES, widget=forms.CheckboxSelectMultiple,)
    

