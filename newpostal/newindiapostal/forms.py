from django import forms

class PincodeForm(forms.Form):
    PINCODE = forms.CharField(max_length=100)
   
