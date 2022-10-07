from django import forms

class user_data(forms.Form):
    name = forms.CharField(max_length=60)
    phone = forms.RegexField(regex='^\(?[1-9]{2}\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$')
    address = forms.CharField(max_length=200)
    
    