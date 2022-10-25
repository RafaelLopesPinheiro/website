from django import forms
from django.forms import ValidationError
from cart.models import Order
from .models import Acompanhamentos, Extra, Quentinha

ACOMP_CHOICES = [
    ('ARROZ_BRANCO','Arroz Branco'),
    ('MACARRAO', 'Macarrão'),
    ('FEIJAO_PRETO', 'Feijão Preto'),
]        

BEBIDA_CHOICES = [
    ('COCA-COLA', 'Coca Cola'),
    ('SPRITE', 'Sprite'),
    ('GUARANA', 'Guaraná'),
    ('FANTA', 'Fanta Laranja')
]


class Bebidas_form(forms.Form):
    bebidas = forms.MultipleChoiceField(choices=BEBIDA_CHOICES,
                                        widget=forms.CheckboxSelectMultiple,
                                        )
    
    def clean(self):
        cleaned_data = super().clean()
        if len(cleaned_data.get('bebidas')) != 1:
            raise ValidationError('You need to choose only one option.')
        


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
    

