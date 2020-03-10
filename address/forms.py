from django import forms

class SearchForm(forms.Form):
    address = forms.CharField(label="Address", max_length=100)