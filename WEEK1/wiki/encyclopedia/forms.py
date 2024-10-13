from django import forms

class SearchForm(forms.Form):
    form = forms.CharField(label="Search")