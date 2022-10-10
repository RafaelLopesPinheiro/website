from django import forms
from .models import Customer
  
    
class customer_data(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'address', 'payment']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'class': 'mask-number'})
        

