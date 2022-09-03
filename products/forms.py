from django import forms

from .models import Acompanhamentos, Extra, Quentinha

ACOMP_CHOICES = [
    ('ARROZ_BRANCO','Arroz Branco'),
    ('MACARRAO', 'Macarrão'),
    ('FEIJAO_PRETO', 'Feijão Preto'),
]        


class Book_form(forms.Form):

    # acompanhamentos = forms.ModelMultipleChoiceField(
    #                     queryset=Acompanhamentos.objects.all(),
    #                     widget=forms.CheckboxSelectMultiple,)
    
    acompanhamentos = forms.ModelMultipleChoiceField(queryset=Acompanhamentos.objects.all(),
                                                     
                    )
    class Meta:
        model = Acompanhamentos
        fields = ['acomp_choices','id']



class Acompanha_Form(forms.ModelForm):
    acompanhamentos = forms.MultipleChoiceField(choices=ACOMP_CHOICES, widget=forms.CheckboxSelectMultiple,)
    

