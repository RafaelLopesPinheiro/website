from django import forms

from .models import Acompanhamentos, Product, Quentinha, Order

        

class QuentinhaForm(forms.ModelForm):
    class Meta:
        model = Acompanhamentos
        fields = ['acomp_choices']
        form_class = forms.ModelMultipleChoiceField(queryset=model.objects.all(), widget=forms.CheckboxSelectMultiple)

    # def clean_titlte(self, *args, **kwargs):
    #     title = self.cleaned_data.get('title')        

CHOICES_ACOMP = [
    ('ARROZ_BRANCO','Arroz Branco'),
    ('MACARRAO', 'Macarrão'),
    ('FEIJAO_PRETO', 'Feijão Preto'),
]


class Book_form(forms.Form):

    acompanhamentos = forms.ModelMultipleChoiceField(
                        queryset=Acompanhamentos.objects.all(),
                        widget=forms.CheckboxSelectMultiple)
    
    observation = forms.TextInput()




class Acompanha_Form(forms.ModelForm):
    acompanhamentos = forms.MultipleChoiceField(choices=CHOICES_ACOMP, widget=forms.CheckboxSelectMultiple,)
    

