from django import forms

class DictionarySearchForm(forms.Form):
    q = forms.CharField(
        label='Search',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search words...'})
    )