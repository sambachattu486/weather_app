from django import forms

class inputField(forms.Form):
    cityName = forms.CharField(max_length=200)