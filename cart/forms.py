from django import forms
from .models import Customer


class user_data(forms.Form):
    name = forms.CharField(max_length=60)
    phone = forms.RegexField(regex='^\(?[1-9]{2}\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$')
    address = forms.CharField(max_length=200)
    
    
class customer_data(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'address', 'payment']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'class': 'mask-number'})