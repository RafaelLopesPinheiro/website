from django import forms
from .models import Customer
  
class Phone_data(forms.ModelForm):
        
    class Meta:
        model = Customer
        fields = ['phone']         

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['phone'].widget.attrs.update({'class': 'mask-number'})
        self.fields['phone'].empty_label = "any type"
  
    
class customer_data(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'payment']
        
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['payment'].widget.select()    
    
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['phone'].widget.attrs.update({'class': 'mask-number'})
        

