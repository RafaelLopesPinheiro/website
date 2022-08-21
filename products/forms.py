from django import forms

from .models import Quentinha

class Quentinha_form(forms.ModelForm):
    class Meta:
        model = Quentinha
        fields = [
            'title',
            'description',
            'price',
        ]
    def clean_titlte(self, *args, **kwargs):
        title = self.cleaned_data.get('title')

        

class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()
    acompanhamentos = forms.BooleanField(required=False)