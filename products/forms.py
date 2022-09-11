from xml.dom import ValidationErr
from django import forms

from .models import Acompanhamentos, Extra, Quentinha

ACOMP_CHOICES = [
    ('ARROZ_BRANCO','Arroz Branco'),
    ('MACARRAO', 'Macarrão'),
    ('FEIJAO_PRETO', 'Feijão Preto'),
]        


class Book_form(forms.Form):

    acompanhamentos = forms.ModelMultipleChoiceField(
                        queryset=Acompanhamentos.objects.all(),
                        )
    
    # acompanhamentos = forms.ModelMultipleChoiceField(queryset=Acompanhamentos.objects.all(),)
    
    class Meta:
        model = Acompanhamentos
        fields = ['acomp_choices','id']
    
    # def clean_acomp_choices(self):
    #     data = self.cleaned_data['acompanhamentos']
    #     if len(data)>3:
    #         raise forms.ValidationError('You cant select more than 3 options.')
        
        # return data    
    


class Acompanha_Form(forms.ModelForm):
    acompanhamentos = forms.MultipleChoiceField(choices=ACOMP_CHOICES, widget=forms.CheckboxSelectMultiple,)
    

