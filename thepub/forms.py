from django import forms


class ShareableForm(forms.Form):
    url = forms.CharField()