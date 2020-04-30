from django import forms


class OnlyForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(max_length=32,widget=forms.PasswordInput)
