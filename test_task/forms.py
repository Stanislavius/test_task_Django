from django import forms

class NameValueForm(forms.Form):
    value = forms.IntegerField(label = "Value")
    name = forms.CharField(label="Name", max_length=100)
    
