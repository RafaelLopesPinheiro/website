from django import forms

from .models import Acomp, Acompanhamentos, Product, Quentinha, Order

ACOMP_CHOICES = [
    ('ARROZ_BRANCO','Arroz Branco'),
    ('MACARRAO', 'Macarrão'),
    ('FEIJAO_PRETO', 'Feijão Preto'),
]        


class QuentinhaForm(forms.ModelForm):
    acomps = forms.MultipleChoiceField(choices=ACOMP_CHOICES, widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Order
        fields = ('acompanhamentos',)     




class Book_form(forms.Form):

    acompanhamentos = forms.ModelMultipleChoiceField(
                        queryset=Acompanhamentos.objects.all(),
                        widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Acompanhamentos
        fields = ['acomp_choices']






class Acompanha_Form(forms.ModelForm):
    acompanhamentos = forms.MultipleChoiceField(choices=ACOMP_CHOICES, widget=forms.CheckboxSelectMultiple,)
    

